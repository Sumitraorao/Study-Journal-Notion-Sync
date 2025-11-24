import reflex as rx
from app.states.journal_state import JournalState


def command_palette() -> rx.Component:
    return rx.cond(
        JournalState.show_command_palette,
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("search", class_name="w-5 h-5 text-gray-400 mr-3"),
                        rx.el.input(
                            placeholder="Type a command or search...",
                            class_name="bg-transparent border-none text-white text-lg placeholder-gray-500 focus:outline-none flex-1",
                            auto_focus=True,
                        ),
                        rx.el.button(
                            "Esc",
                            on_click=JournalState.toggle_command_palette,
                            class_name="text-xs text-gray-500 border border-gray-700 px-1.5 py-0.5 rounded",
                        ),
                        class_name="flex items-center border-b border-white/10 p-4",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                "Actions",
                                class_name="text-xs font-medium text-gray-500 mb-2 block",
                            ),
                            rx.el.button(
                                rx.icon(
                                    "plus", class_name="w-4 h-4 mr-2 text-gray-400"
                                ),
                                "New Thread",
                                on_click=[
                                    rx.set_focus("search-input"),
                                    JournalState.toggle_command_palette,
                                ],
                                class_name="flex items-center w-full p-2 rounded-lg hover:bg-white/5 text-gray-300 text-sm transition-colors text-left",
                            ),
                            rx.el.button(
                                rx.icon(
                                    "moon", class_name="w-4 h-4 mr-2 text-gray-400"
                                ),
                                "Toggle Theme",
                                class_name="flex items-center w-full p-2 rounded-lg hover:bg-white/5 text-gray-300 text-sm transition-colors text-left",
                            ),
                        ),
                        class_name="p-4",
                    ),
                    class_name="bg-[#18181b] border border-white/10 rounded-xl shadow-2xl w-full max-w-xl overflow-hidden",
                    on_click=lambda: rx.noop(),
                ),
                class_name="fixed inset-0 z-50 flex items-start justify-center pt-[20vh] px-4 animate-fade-in",
            ),
            rx.el.div(
                class_name="fixed inset-0 bg-black/60 backdrop-blur-sm z-40",
                on_click=JournalState.toggle_command_palette,
            ),
            class_name="relative z-50",
        ),
    )