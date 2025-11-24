import reflex as rx
from app.states.journal_state import JournalState


def focus_mode_chip(mode: str) -> rx.Component:
    is_selected = JournalState.focus_mode == mode
    return rx.el.button(
        mode,
        on_click=lambda: JournalState.set_focus_mode(mode),
        type="button",
        class_name=rx.cond(
            is_selected,
            "px-3 py-1 rounded-full text-xs font-medium bg-cyan-500/20 text-cyan-400 border border-cyan-500/50 transition-all",
            "px-3 py-1 rounded-full text-xs font-medium text-gray-400 border border-white/10 hover:bg-white/5 hover:text-gray-200 transition-all",
        ),
    )


def question_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Where knowledge begins",
                class_name="text-3xl md:text-4xl font-medium text-white mb-8 text-center tracking-tight",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.div(
                        rx.el.textarea(
                            id="search-input",
                            placeholder="Ask anything...",
                            on_change=JournalState.set_current_question,
                            name="question",
                            rows=1,
                            disabled=JournalState.is_loading,
                            class_name="w-full bg-transparent border-none text-lg text-white placeholder-gray-500 focus:ring-0 focus:outline-none resize-none py-3 px-4 min-h-[60px] max-h-[200px]",
                            default_value=JournalState.current_question,
                        ),
                        class_name="w-full",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                "Focus",
                                class_name="text-xs font-semibold text-gray-500 uppercase tracking-wider mr-3",
                            ),
                            rx.el.div(
                                rx.foreach(
                                    JournalState.available_focus_modes, focus_mode_chip
                                ),
                                class_name="flex flex-wrap gap-2",
                            ),
                            class_name="flex items-center flex-wrap gap-y-2",
                        ),
                        rx.el.button(
                            rx.cond(
                                JournalState.is_loading,
                                rx.spinner(size="2", class_name="text-white"),
                                rx.icon("arrow-right", class_name="w-5 h-5 text-white"),
                            ),
                            type="submit",
                            disabled=JournalState.is_loading,
                            class_name="p-2 rounded-full bg-cyan-600 hover:bg-cyan-500 disabled:bg-gray-700 disabled:cursor-not-allowed transition-colors flex items-center justify-center shadow-lg shrink-0 ml-4",
                        ),
                        class_name="flex justify-between items-end border-t border-white/10 pt-3 mt-2",
                    ),
                    class_name="bg-[#202023] rounded-2xl border border-white/10 p-4 shadow-2xl focus-within:border-cyan-500/50 transition-colors",
                ),
                on_submit=JournalState.submit_question,
                class_name="max-w-2xl mx-auto w-full relative z-10",
            ),
            class_name="flex flex-col items-center justify-center py-12",
        ),
        class_name="w-full",
    )