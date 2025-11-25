import reflex as rx
from app.components.nft_navbar import nft_navbar
from app.components.nft_detail_components import (
    detail_header,
    price_card,
    bid_input_section,
    details_tabs,
    related_carousel,
)
from app.states.nft_detail_state import NFTDetailState


def nft_image_display() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="absolute inset-0 bg-gradient-to-br from-purple-600/20 to-cyan-600/20 rounded-3xl blur-3xl -z-10"
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "rocket",
                    class_name="w-64 h-64 text-white/80 drop-shadow-[0_0_30px_rgba(255,255,255,0.3)] animate-pulse duration-[3000ms]",
                ),
                class_name="absolute inset-0 flex items-center justify-center",
            ),
            rx.el.button(
                rx.icon(
                    "heart",
                    class_name=rx.cond(
                        NFTDetailState.is_liked,
                        "fill-pink-500 text-pink-500",
                        "text-white",
                    ),
                ),
                rx.el.span(
                    NFTDetailState.likes, class_name="ml-2 text-sm font-bold text-white"
                ),
                on_click=NFTDetailState.toggle_like,
                class_name="absolute top-6 right-6 bg-black/40 backdrop-blur-md border border-white/10 py-2 px-4 rounded-full flex items-center hover:bg-black/60 transition-all hover:scale-105 z-20",
            ),
            rx.el.div(
                rx.el.span(
                    "Live Auction",
                    class_name="uppercase text-[10px] font-bold tracking-wider text-white animate-pulse",
                ),
                class_name="absolute top-6 left-6 bg-red-500/80 backdrop-blur-md py-1.5 px-3 rounded-md z-20",
            ),
            class_name="relative w-full aspect-square rounded-3xl bg-gradient-to-br from-indigo-900 via-purple-900 to-slate-900 overflow-hidden shadow-2xl border border-white/5 group",
        ),
        class_name="sticky top-24",
    )


def nft_detail_page() -> rx.Component:
    return rx.el.div(
        nft_navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(nft_image_display(), class_name="lg:col-span-5"),
                rx.el.div(
                    detail_header(),
                    rx.el.p(
                        NFTDetailState.description,
                        class_name="text-gray-400 leading-relaxed mb-8 text-lg font-light",
                    ),
                    price_card(),
                    bid_input_section(),
                    details_tabs(),
                    class_name="lg:col-span-7 flex flex-col",
                ),
                class_name="max-w-[1440px] mx-auto px-6 grid grid-cols-1 lg:grid-cols-12 gap-12 pt-32 pb-20",
            ),
            rx.el.div(related_carousel(), class_name="max-w-[1440px] mx-auto px-6"),
            class_name="min-h-screen bg-[#0f0f10]",
        ),
        rx.window_event_listener(on_mount=NFTDetailState.on_load_nft),
        class_name="bg-[#0f0f10] min-h-screen font-['Inter'] selection:bg-cyan-500/30",
    )