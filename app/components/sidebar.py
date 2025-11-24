import reflex as rx
from app.states.journal_state import JournalState, JournalEntry


def sidebar_item(entry: JournalEntry) -> rx.Component:
    return rx.el.button(
        rx.icon("message-square", class_name="w-4 h-4 text-gray-400 shrink-0"),
        rx.el.span(
            entry["question"],
            class_name="truncate text-sm text-gray-300 group-hover:text-white transition-colors text-left flex-1",
        ),
        class_name="group flex items-center gap-3 w-full px-3 py-2 rounded-lg hover:bg-white/5 transition-colors",
    )


def group_section(group_name: str, entries: list[JournalEntry]) -> rx.Component:
    return rx.cond(
        entries,
        rx.el.div(
            rx.el.h4(
                group_name,
                class_name="text-[10px] font-bold text-gray-500 uppercase tracking-wider px-4 mb-2 mt-4",
            ),
            rx.foreach(entries, sidebar_item),
            class_name="mb-2",
        ),
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.icon("library", class_name="w-8 h-8 text-cyan-400"),
            rx.el.span(
                "PerplexJournal",
                class_name="text-xl font-bold text-white tracking-tight",
            ),
            class_name="flex items-center gap-3 px-4 py-6 mb-2",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("plus", class_name="w-4 h-4 mr-2"),
                "New Thread",
                on_click=rx.set_focus("search-input"),
                class_name="flex items-center justify-center w-full py-2 px-4 bg-white/10 hover:bg-white/20 text-white rounded-full border border-white/10 transition-all text-sm font-medium mb-6",
            ),
            class_name="px-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Library",
                    class_name="text-xs font-bold text-gray-500 uppercase tracking-wider px-4 mb-2 block",
                ),
                rx.el.nav(
                    rx.el.a(
                        rx.icon("compass", class_name="w-4 h-4 mr-3"),
                        "Discover",
                        href="#",
                        class_name="flex items-center px-4 py-2 text-sm text-gray-300 hover:text-white hover:bg-white/5 rounded-lg transition-colors",
                    ),
                    rx.el.button(
                        rx.icon("command", class_name="w-4 h-4 mr-3"),
                        "Commands",
                        on_click=JournalState.toggle_command_palette,
                        class_name="flex w-full items-center px-4 py-2 text-sm text-gray-300 hover:text-white hover:bg-white/5 rounded-lg transition-colors",
                    ),
                    class_name="space-y-1 mb-6 px-2",
                ),
            ),
            rx.el.div(
                rx.el.span(
                    "History",
                    class_name="text-xs font-bold text-gray-500 uppercase tracking-wider px-4 mb-2 block",
                ),
                rx.el.div(
                    group_section("Today", JournalState.grouped_history["Today"]),
                    group_section(
                        "Yesterday", JournalState.grouped_history["Yesterday"]
                    ),
                    group_section(
                        "Previous 7 Days",
                        JournalState.grouped_history["Previous 7 Days"],
                    ),
                    group_section("Older", JournalState.grouped_history["Older"]),
                    class_name="space-y-1 px-2 overflow-y-auto max-h-[calc(100vh-300px)] custom-scrollbar",
                ),
            ),
            class_name="flex-1 overflow-hidden flex flex-col",
        ),
        rx.el.div(
            rx.el.button(
                rx.el.div(
                    rx.icon("user", class_name="w-4 h-4 text-white"),
                    class_name="w-8 h-8 rounded-full bg-gradient-to-tr from-purple-500 to-cyan-500 flex items-center justify-center",
                ),
                rx.el.div(
                    rx.el.span(
                        "User Account",
                        class_name="text-sm font-medium text-white block text-left",
                    ),
                    rx.el.span(
                        "Free Plan", class_name="text-xs text-gray-400 block text-left"
                    ),
                    class_name="ml-3",
                ),
                class_name="flex items-center w-full p-2 rounded-lg hover:bg-white/5 transition-colors",
            ),
            class_name="p-4 border-t border-white/5",
        ),
        class_name="hidden md:flex flex-col w-64 bg-[#18181b] border-r border-white/10 h-screen sticky top-0 shrink-0",
    )