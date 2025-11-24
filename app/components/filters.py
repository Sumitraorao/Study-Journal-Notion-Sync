import reflex as rx
from app.states.journal_state import JournalState


def filter_tag_chip(tag: str) -> rx.Component:
    is_selected = JournalState.filter_tags.contains(tag)
    return rx.el.button(
        tag,
        on_click=lambda: JournalState.toggle_filter_tag(tag),
        class_name=rx.cond(
            is_selected,
            "px-3 py-1 rounded-full text-sm font-medium bg-cyan-500/20 text-cyan-400 border border-cyan-500/50 transition-colors",
            "px-3 py-1 rounded-full text-sm font-medium bg-white/5 text-gray-400 border border-white/10 hover:bg-white/10 transition-colors",
        ),
    )


def filters_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Filters",
                class_name="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Date Range",
                    class_name="block text-sm font-medium text-gray-300 mb-2",
                ),
                rx.el.div(
                    rx.el.input(
                        type="date",
                        on_change=JournalState.set_date_start,
                        class_name="block w-full rounded-md border-white/10 bg-white/5 px-3 py-2 text-sm text-white shadow-sm focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500",
                        default_value=JournalState.date_start,
                    ),
                    rx.el.span("to", class_name="text-gray-500 text-sm"),
                    rx.el.input(
                        type="date",
                        on_change=JournalState.set_date_end,
                        class_name="block w-full rounded-md border-white/10 bg-white/5 px-3 py-2 text-sm text-white shadow-sm focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500",
                        default_value=JournalState.date_end,
                    ),
                    class_name="flex items-center gap-2 mb-6",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Filter by Tags",
                        class_name="block text-sm font-medium text-gray-300",
                    ),
                    rx.cond(
                        JournalState.has_active_filters,
                        rx.el.button(
                            "Clear All",
                            on_click=JournalState.clear_filters,
                            class_name="text-xs text-cyan-400 hover:text-cyan-300 font-medium",
                        ),
                    ),
                    class_name="flex justify-between items-center mb-2",
                ),
                rx.el.div(
                    rx.foreach(JournalState.available_tags, filter_tag_chip),
                    class_name="flex flex-wrap gap-2",
                ),
            ),
            class_name="bg-[#202023] p-5 rounded-xl shadow-sm border border-white/5",
        ),
        class_name="w-full lg:w-80 shrink-0 space-y-6",
    )