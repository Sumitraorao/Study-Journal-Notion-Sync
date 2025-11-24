import reflex as rx
from app.states.journal_state import JournalEntry, JournalState, JournalTurn
from app.components.citation import citation_card


def tag_badge(tag: str) -> rx.Component:
    return rx.el.span(
        tag,
        class_name="inline-flex items-center px-2.5 py-0.5 rounded-md text-[10px] font-medium bg-white/5 text-gray-300 border border-white/10",
    )


def related_question_chip(question: str) -> rx.Component:
    return rx.el.button(
        rx.icon("plus", class_name="w-3 h-3 text-gray-400 mr-2"),
        rx.el.span(question, class_name="text-sm text-gray-300 truncate"),
        on_click=lambda: JournalState.regenerate_entry(question),
        class_name="flex items-center w-full px-4 py-2 bg-white/5 hover:bg-white/10 border border-white/5 rounded-lg transition-colors text-left",
    )


def message_bubble(turn: JournalTurn, index: int) -> rx.Component:
    is_user = turn["role"] == "user"
    return rx.el.div(
        rx.el.div(
            rx.cond(
                is_user,
                rx.icon("user", class_name="w-5 h-5 text-gray-400 mt-1 shrink-0"),
                rx.icon("sparkles", class_name="w-5 h-5 text-cyan-400 mt-1 shrink-0"),
            ),
            class_name=rx.cond(
                is_user,
                "p-1.5 bg-gray-700/30 rounded-lg h-fit shrink-0",
                "p-1.5 bg-cyan-500/10 rounded-lg h-fit shrink-0",
            ),
        ),
        rx.el.div(
            rx.cond(
                is_user,
                rx.el.p(
                    turn["content"], class_name="text-white text-lg font-medium mb-2"
                ),
                rx.el.div(
                    rx.markdown(
                        turn["content"],
                        component_map={
                            "p": lambda text: rx.el.p(
                                text,
                                class_name="text-gray-300 leading-relaxed mb-4 font-light text-[15px]",
                            )
                        },
                        class_name="prose prose-invert max-w-none",
                    ),
                    rx.cond(
                        turn["citations"].length() > 0,
                        rx.el.div(
                            rx.el.h4(
                                "Sources",
                                class_name="text-xs font-bold text-gray-500 uppercase tracking-wider mb-3 mt-4",
                            ),
                            rx.el.div(
                                rx.foreach(
                                    turn["citations"],
                                    lambda src, idx: citation_card(idx, src),
                                ),
                                class_name="flex gap-3 overflow-x-auto pb-2 custom-scrollbar",
                            ),
                        ),
                    ),
                ),
            ),
            class_name="ml-4 w-full min-w-0",
        ),
        class_name=rx.cond(
            is_user,
            "flex items-start pt-6 border-t border-white/5",
            "flex items-start pt-4",
        ),
    )


def entry_card(entry: JournalEntry) -> rx.Component:
    return rx.el.article(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        entry["question"],
                        class_name="text-xl font-semibold text-white leading-snug tracking-tight",
                    ),
                    rx.el.span(
                        entry["created_at"].split("T")[0],
                        class_name="text-xs font-medium text-gray-500 ml-4 shrink-0 font-mono",
                    ),
                    class_name="flex justify-between items-start w-full",
                ),
                class_name="mb-6 border-b border-white/5 pb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "sparkles", class_name="w-5 h-5 text-cyan-400 mt-1 shrink-0"
                        ),
                        class_name="p-1.5 bg-cyan-500/10 rounded-lg h-fit shrink-0",
                    ),
                    rx.el.div(
                        rx.markdown(
                            entry["answer"], class_name="prose prose-invert max-w-none"
                        ),
                        rx.cond(
                            entry["citations"].length() > 0,
                            rx.el.div(
                                rx.el.h4(
                                    "Sources",
                                    class_name="text-xs font-bold text-gray-500 uppercase tracking-wider mb-3 mt-6",
                                ),
                                rx.el.div(
                                    rx.foreach(
                                        entry["citations"],
                                        lambda src, idx: citation_card(idx, src),
                                    ),
                                    class_name="flex gap-3 overflow-x-auto pb-2 custom-scrollbar",
                                ),
                            ),
                        ),
                        class_name="ml-4 w-full min-w-0",
                    ),
                    class_name="flex items-start",
                ),
                rx.cond(
                    entry["history"],
                    rx.el.div(
                        rx.foreach(
                            entry["history"], lambda turn, i: message_bubble(turn, i)
                        ),
                        class_name="space-y-4 mt-6",
                    ),
                ),
                rx.cond(
                    JournalState.loading_entries.contains(entry["id"]),
                    rx.el.div(
                        rx.el.div(
                            class_name="animate-pulse w-8 h-8 bg-gray-700 rounded-full shrink-0"
                        ),
                        rx.el.div(
                            rx.el.div(class_name="h-4 bg-gray-700 rounded w-3/4 mb-2"),
                            rx.el.div(class_name="h-4 bg-gray-700 rounded w-1/2"),
                            class_name="ml-4 w-full animate-pulse",
                        ),
                        class_name="flex items-start mt-6",
                    ),
                ),
                rx.el.div(
                    rx.el.input(
                        placeholder="Ask a follow up...",
                        on_change=lambda val: JournalState.set_followup_input(
                            entry["id"], val
                        ),
                        on_key_down=lambda k: rx.cond(
                            k == "Enter",
                            JournalState.submit_followup(entry["id"]),
                            rx.noop(),
                        ),
                        class_name="w-full bg-[#18181b] border border-white/5 rounded-full py-2.5 px-4 text-sm text-white placeholder-gray-500 focus:ring-1 focus:ring-cyan-500 focus:border-cyan-500 outline-none transition-all",
                        default_value=JournalState.followup_input[entry["id"]],
                    ),
                    rx.el.button(
                        rx.icon("arrow-up", class_name="w-4 h-4"),
                        on_click=lambda: JournalState.submit_followup(entry["id"]),
                        class_name="absolute right-2 top-1/2 -translate-y-1/2 p-1.5 bg-white/10 hover:bg-white/20 text-gray-300 rounded-full transition-colors",
                    ),
                    class_name="mt-8 relative",
                ),
                rx.cond(
                    entry["related_questions"].length() > 0,
                    rx.el.div(
                        rx.el.h4(
                            "Related",
                            class_name="text-xs font-bold text-gray-500 uppercase tracking-wider mb-3 mt-6",
                        ),
                        rx.el.div(
                            rx.foreach(
                                entry["related_questions"], related_question_chip
                            ),
                            class_name="grid grid-cols-1 gap-2",
                        ),
                    ),
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.foreach(entry["tags"], tag_badge),
                    class_name="flex gap-2 flex-wrap",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon("copy", class_name="w-4 h-4"),
                        on_click=rx.set_clipboard(entry["answer"]),
                        class_name="p-2 text-gray-500 hover:text-white hover:bg-white/5 rounded-lg transition-all",
                        title="Copy answer",
                    ),
                    rx.el.button(
                        rx.icon("download", class_name="w-4 h-4"),
                        on_click=lambda: JournalState.export_entry(entry["id"]),
                        class_name="p-2 text-gray-500 hover:text-white hover:bg-white/5 rounded-lg transition-all",
                        title="Export Markdown",
                    ),
                    rx.el.button(
                        rx.icon("share-2", class_name="w-4 h-4"),
                        class_name="p-2 text-gray-500 hover:text-white hover:bg-white/5 rounded-lg transition-all",
                        title="Share",
                    ),
                    class_name="flex items-center gap-1",
                ),
                class_name="flex justify-between items-center mt-8 pt-6 border-t border-white/5",
            ),
            class_name="p-6 md:p-8",
        ),
        class_name="bg-[#202023] rounded-2xl border border-white/5 hover:border-white/10 transition-all duration-500 shadow-xl animate-fade-in overflow-hidden group",
    )