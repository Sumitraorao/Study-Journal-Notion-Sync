import reflex as rx
from app.states.journal_state import JournalState
from app.components.question_form import question_form
from app.components.entry_card import entry_card
from app.components.sidebar import sidebar
from app.components.navbar import navbar
from app.components.filters import filters_section
from app.components.command_palette import command_palette
from app.pages.nft_landing import nft_landing


def skeleton_loader() -> rx.Component:
    return rx.el.div(
        rx.el.div(class_name="w-3/4 h-8 bg-white/5 rounded animate-pulse mb-4"),
        rx.el.div(class_name="w-full h-32 bg-white/5 rounded animate-pulse mb-4"),
        rx.el.div(
            rx.el.div(class_name="w-1/4 h-4 bg-white/5 rounded animate-pulse"),
            rx.el.div(class_name="w-1/4 h-4 bg-white/5 rounded animate-pulse"),
            class_name="flex gap-4",
        ),
        class_name="bg-[#202023] p-6 rounded-2xl border border-white/5",
    )


def empty_state() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("search", class_name="w-12 h-12 text-gray-700 mb-4"),
            rx.el.h3("Ready to explore?", class_name="text-lg font-medium text-white"),
            rx.el.p(
                "Start by asking a question above.", class_name="text-gray-500 mt-1"
            ),
            class_name="flex flex-col items-center justify-center py-12 px-4 text-center",
        ),
        class_name="rounded-xl border border-dashed border-white/10 bg-white/5",
    )


def index() -> rx.Component:
    return rx.el.div(
        rx.window_event_listener(on_key_down=JournalState.handle_key_down),
        command_palette(),
        sidebar(),
        rx.el.div(
            navbar(),
            rx.el.main(
                rx.el.div(
                    question_form(),
                    rx.el.div(
                        rx.cond(
                            JournalState.has_entries | JournalState.is_loading,
                            rx.el.div(
                                rx.el.div(
                                    rx.icon(
                                        "clock", class_name="w-5 h-5 text-cyan-400"
                                    ),
                                    rx.el.h2(
                                        "Recent Activity",
                                        class_name="text-xl font-semibold text-white",
                                    ),
                                    class_name="flex items-center gap-2 mb-6",
                                ),
                                rx.el.div(
                                    filters_section(),
                                    rx.el.div(
                                        rx.cond(
                                            JournalState.is_loading, skeleton_loader()
                                        ),
                                        rx.foreach(
                                            JournalState.filtered_entries, entry_card
                                        ),
                                        class_name="grid grid-cols-1 lg:grid-cols-2 gap-6 flex-1",
                                    ),
                                    class_name="flex flex-col xl:flex-row gap-6 items-start",
                                ),
                                class_name="animate-fade-in",
                            ),
                            empty_state(),
                        ),
                        class_name="max-w-screen-2xl mx-auto",
                    ),
                    class_name="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-12",
                ),
                class_name="flex-1 overflow-y-auto bg-[#0f0f10]",
            ),
            class_name="flex-1 flex flex-col h-screen min-w-0",
        ),
        class_name="flex min-h-screen bg-[#0f0f10] font-['Inter'] text-gray-200",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
from app.pages.nft_detail import nft_detail_page
from app.pages.profile import profile_page
from app.pages.create_nft import create_nft_page
from app.pages.settings import settings_page

app.add_page(nft_landing, route="/")
app.add_page(index, route="/journal")
app.add_page(nft_detail_page, route="/nft/[id]")
app.add_page(profile_page, route="/profile")
app.add_page(create_nft_page, route="/create")
app.add_page(settings_page, route="/settings")