import reflex as rx
from datetime import datetime
from typing import TypedDict
import os
import logging
import uuid
import httpx
import re


class JournalTurn(TypedDict):
    role: str
    content: str
    citations: list[str]
    related_questions: list[str]
    created_at: str


class JournalEntry(TypedDict):
    id: str
    question: str
    answer: str
    tags: list[str]
    citations: list[str]
    related_questions: list[str]
    created_at: str
    history: list[JournalTurn]


class JournalState(rx.State):
    entries: list[JournalEntry] = []
    current_question: str = ""
    followup_input: dict[str, str] = {}
    loading_entries: list[str] = []
    show_command_palette: bool = False
    current_tags: list[str] = []
    filter_tags: list[str] = []
    date_start: str = ""
    date_end: str = ""
    available_tags: list[str] = ["Coding", "Math", "History", "Science", "Literature"]
    focus_mode: str = "All"
    available_focus_modes: list[str] = [
        "All",
        "Academic",
        "Writing",
        "Math",
        "Coding",
        "Science",
        "History",
    ]
    is_loading: bool = False

    @rx.event
    def set_focus_mode(self, mode: str):
        self.focus_mode = mode

    @rx.event
    def set_current_question(self, value: str):
        self.current_question = value

    @rx.event
    def toggle_current_tag(self, tag: str):
        if tag in self.current_tags:
            self.current_tags.remove(tag)
        else:
            self.current_tags.append(tag)

    @rx.event
    def toggle_filter_tag(self, tag: str):
        if tag in self.filter_tags:
            self.filter_tags.remove(tag)
        else:
            self.filter_tags.append(tag)

    @rx.event
    def set_date_start(self, value: str):
        self.date_start = value

    @rx.event
    def set_date_end(self, value: str):
        self.date_end = value

    @rx.event
    def clear_filters(self):
        self.filter_tags = []
        self.date_start = ""
        self.date_end = ""

    @rx.event
    def regenerate_entry(self, question: str):
        self.current_question = question
        return JournalState.submit_question

    @rx.event
    def set_followup_input(self, entry_id: str, value: str):
        self.followup_input[entry_id] = value

    @rx.event
    def toggle_command_palette(self):
        self.show_command_palette = not self.show_command_palette

    @rx.event
    def handle_key_down(self, key: str):
        if key == "/":
            return rx.set_focus("search-input")

    @rx.event
    def export_entry(self, entry_id: str):
        entry = next((e for e in self.entries if e["id"] == entry_id), None)
        if not entry:
            return
        content = f"# {entry['question']}\n\n{entry['answer']}\n\n"
        if entry.get("history"):
            for turn in entry["history"]:
                if turn["role"] == "user":
                    content += f"## Q: {turn['content']}\n\n"
                else:
                    content += f"{turn['content']}\n\n"
        if entry["citations"]:
            content += """## Sources
"""
            for src in entry["citations"]:
                content += f"- {src}\n"
        return rx.download(data=content, filename=f"entry-{entry_id[:8]}.md")

    @rx.event
    async def submit_question(self, form_data: dict):
        if not self.current_question.strip():
            yield rx.toast("Please enter a question", position="bottom-right")
            return
        self.is_loading = True
        yield
        api_key = os.getenv("PERPLEXITY_API_KEY")
        if not api_key:
            self.is_loading = False
            yield rx.toast("Error: PERPLEXITY_API_KEY not set", position="bottom-right")
            return
        try:
            async with httpx.AsyncClient() as client:
                payload = {
                    "model": "sonar",
                    "messages": [
                        {
                            "role": "system",
                            "content": "You are a helpful learning assistant. Provide clear, concise answers in Markdown format. At the very end of your answer, always add a section titled '### Related Questions' followed by exactly 3 distinct follow-up questions as bullet points.",
                        },
                        {"role": "user", "content": self.current_question},
                    ],
                }
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                }
                response = await client.post(
                    "https://api.perplexity.ai/chat/completions",
                    json=payload,
                    headers=headers,
                    timeout=60.0,
                )
                response.raise_for_status()
                data = response.json()
                content = data["choices"][0]["message"]["content"]
                citations = data.get("citations", [])
                related_questions = []
                clean_answer = content
                split_pattern = "### Related Questions"
                parts = re.split(split_pattern, content, flags=re.IGNORECASE)
                if len(parts) > 1:
                    clean_answer = parts[0].strip()
                    raw_related = parts[1].strip()
                    for line in raw_related.split("""
"""):
                        clean_line = line.strip()
                        if (
                            clean_line.startswith("- ")
                            or clean_line.startswith("* ")
                            or (
                                clean_line
                                and clean_line[0].isdigit()
                                and (clean_line[1] == ".")
                            )
                        ):
                            clean_text = re.sub(
                                "^[-*\\d.]+\\s*", "", clean_line
                            ).strip()
                            if clean_text:
                                related_questions.append(clean_text)
                new_entry: JournalEntry = {
                    "id": str(uuid.uuid4()),
                    "question": self.current_question,
                    "answer": clean_answer,
                    "tags": self.current_tags if self.current_tags else ["General"],
                    "citations": citations,
                    "related_questions": related_questions[:3],
                    "created_at": datetime.now().isoformat(),
                    "history": [],
                }
                self.entries.insert(0, new_entry)
                self.current_question = ""
                self.current_tags = []
                yield rx.toast("Entry added successfully", position="bottom-right")
        except Exception as e:
            logging.exception("Perplexity API Error")
            yield rx.toast(f"Error querying AI: {str(e)}", position="bottom-right")
        finally:
            self.is_loading = False

    @rx.event
    async def submit_followup(self, entry_id: str):
        entry_index = -1
        for i, e in enumerate(self.entries):
            if e["id"] == entry_id:
                entry_index = i
                break
        if entry_index == -1:
            return
        entry = self.entries[entry_index]
        question_text = self.followup_input.get(entry_id, "")
        if not question_text.strip():
            return
        self.loading_entries.append(entry_id)
        yield
        try:
            api_key = os.getenv("PERPLEXITY_API_KEY")
            if not api_key:
                yield rx.toast("Error: API Key missing", position="bottom-right")
                return
            messages = [
                {
                    "role": "system",
                    "content": "You are a helpful learning assistant. Be concise.",
                },
                {"role": "user", "content": entry["question"]},
                {"role": "assistant", "content": entry["answer"]},
            ]
            if "history" in entry:
                for turn in entry["history"]:
                    messages.append({"role": turn["role"], "content": turn["content"]})
            messages.append({"role": "user", "content": question_text})
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://api.perplexity.ai/chat/completions",
                    json={"model": "sonar", "messages": messages},
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                    },
                    timeout=60.0,
                )
                response.raise_for_status()
                data = response.json()
                content = data["choices"][0]["message"]["content"]
                citations = data.get("citations", [])
                user_turn: JournalTurn = {
                    "role": "user",
                    "content": question_text,
                    "citations": [],
                    "related_questions": [],
                    "created_at": datetime.now().isoformat(),
                }
                ai_turn: JournalTurn = {
                    "role": "assistant",
                    "content": content,
                    "citations": citations,
                    "related_questions": [],
                    "created_at": datetime.now().isoformat(),
                }
                if "history" not in self.entries[entry_index]:
                    self.entries[entry_index]["history"] = []
                self.entries[entry_index]["history"].extend([user_turn, ai_turn])
                self.followup_input[entry_id] = ""
        except Exception as e:
            logging.exception("Follow-up Error")
            yield rx.toast(f"Error: {str(e)}", position="bottom-right")
        finally:
            if entry_id in self.loading_entries:
                self.loading_entries.remove(entry_id)

    @rx.var
    def filtered_entries(self) -> list[JournalEntry]:
        filtered = self.entries
        if self.filter_tags:
            filtered = [
                entry
                for entry in filtered
                if any((tag in self.filter_tags for tag in entry["tags"]))
            ]
        if self.date_start:
            filtered = [
                entry
                for entry in filtered
                if entry["created_at"][:10] >= self.date_start
            ]
        if self.date_end:
            filtered = [
                entry for entry in filtered if entry["created_at"][:10] <= self.date_end
            ]
        return filtered

    @rx.var
    def has_entries(self) -> bool:
        return len(self.filtered_entries) > 0

    @rx.var
    def has_active_filters(self) -> bool:
        return bool(self.filter_tags) or bool(self.date_start) or bool(self.date_end)

    @rx.var
    def grouped_history(self) -> dict[str, list[JournalEntry]]:
        today = datetime.now().date()
        groups = {"Today": [], "Yesterday": [], "Previous 7 Days": [], "Older": []}
        for entry in self.entries:
            try:
                created = datetime.fromisoformat(entry["created_at"]).date()
                days_diff = (today - created).days
                if days_diff == 0:
                    groups["Today"].append(entry)
                elif days_diff == 1:
                    groups["Yesterday"].append(entry)
                elif days_diff <= 7:
                    groups["Previous 7 Days"].append(entry)
                else:
                    groups["Older"].append(entry)
            except ValueError:
                logging.exception("Error parsing date in grouped_history")
                groups["Older"].append(entry)
        return groups