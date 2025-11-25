import reflex as rx
from app.states.nft_state import NftState, Creator


def artwork_thumbnail(gradient: str, index: int) -> rx.Component:
    return rx.el.div(
        class_name=f"w-full h-16 rounded-lg bg-gradient-to-br {gradient} shadow-inner transform transition-transform hover:scale-105 duration-300"
    )


def creator_card(creator: Creator) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name=f"h-24 w-full bg-gradient-to-r {creator['cover_gradient']} rounded-t-2xl"
        ),
        rx.el.div(
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/notionists/svg?seed={creator['avatar_seed']}",
                    class_name="w-16 h-16 rounded-full bg-[#1a1a1e]",
                ),
                class_name="absolute -top-8 left-6 p-1 bg-[#1a1a1e] rounded-full",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        creator["name"],
                        class_name="text-lg font-bold text-white truncate",
                    ),
                    rx.el.p(
                        creator["handle"], class_name="text-sm text-gray-400 truncate"
                    ),
                ),
                rx.el.button(
                    rx.cond(creator["is_followed"], "Following", "Follow"),
                    on_click=lambda: NftState.toggle_follow(creator["id"]),
                    class_name=rx.cond(
                        creator["is_followed"],
                        "px-4 py-1.5 rounded-full bg-white/10 text-white text-xs font-bold hover:bg-white/20 transition-all",
                        "px-4 py-1.5 rounded-full bg-white text-black text-xs font-bold hover:bg-gray-200 transition-all shadow-[0_0_15px_rgba(255,255,255,0.3)]",
                    ),
                ),
                class_name="flex justify-between items-start mt-10 px-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Collections",
                        class_name="text-xs text-gray-500 uppercase font-semibold",
                    ),
                    rx.el.p(
                        creator["collection_value"],
                        class_name="text-sm font-bold text-white",
                    ),
                ),
                rx.el.div(
                    rx.el.p(
                        "Followers",
                        class_name="text-xs text-gray-500 uppercase font-semibold",
                    ),
                    rx.el.p(
                        creator["followers"], class_name="text-sm font-bold text-white"
                    ),
                ),
                class_name="flex gap-8 px-6 mt-6 mb-6",
            ),
            rx.el.div(
                rx.foreach(
                    creator["artwork_gradients"],
                    lambda grad, i: artwork_thumbnail(grad, i),
                ),
                rx.el.div(
                    rx.el.span("+25", class_name="text-xs font-bold text-white"),
                    class_name="absolute right-0 top-0 bottom-0 w-1/3 bg-black/60 backdrop-blur-sm flex items-center justify-center rounded-r-lg hover:bg-black/70 transition-colors cursor-pointer",
                ),
                class_name="grid grid-cols-3 gap-2 px-6 pb-6 relative overflow-hidden",
            ),
            class_name="relative",
        ),
        class_name="bg-[#1a1a1e] rounded-2xl overflow-hidden border border-white/5 hover:border-white/20 hover:-translate-y-2 hover:shadow-2xl hover:shadow-purple-500/10 transition-all duration-500 group",
    )


def top_creators_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Top creators this month",
                class_name="text-3xl md:text-4xl font-bold text-white mb-12",
            ),
            rx.el.div(
                rx.foreach(NftState.top_creators, creator_card),
                class_name="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6",
            ),
            class_name="max-w-[1440px] mx-auto px-6 w-full",
        ),
        class_name="py-20 bg-[#0f0f10]",
    )