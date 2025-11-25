import reflex as rx
from app.states.nft_state import NftState, NFTListing


def category_tab(category: str) -> rx.Component:
    return rx.el.button(
        category,
        on_click=lambda: NftState.set_active_category(category),
        class_name=rx.cond(
            NftState.active_category == category,
            "px-6 py-2 rounded-full bg-[#56E1F6] text-black font-bold text-sm transition-all shadow-[0_0_15px_rgba(86,225,246,0.4)] transform scale-105",
            "px-6 py-2 rounded-full bg-white/5 text-gray-400 font-medium text-sm hover:bg-white/10 hover:text-white transition-all border border-white/5",
        ),
    )


def skeleton_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(class_name="w-full aspect-square bg-white/5 animate-pulse"),
        rx.el.div(
            rx.el.div(class_name="h-6 w-3/4 bg-white/5 rounded animate-pulse mb-2"),
            rx.el.div(class_name="h-4 w-1/2 bg-white/5 rounded animate-pulse mb-6"),
            rx.el.div(
                rx.el.div(class_name="h-10 flex-1 bg-white/5 rounded animate-pulse"),
                rx.el.div(class_name="h-10 flex-1 bg-white/5 rounded animate-pulse"),
                class_name="flex gap-3",
            ),
            class_name="p-5",
        ),
        class_name="rounded-2xl overflow-hidden bg-[#1a1a1e] border border-white/5",
    )


def nft_card(listing: NFTListing) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        listing["category"],
                        class_name="px-3 py-1 rounded-full bg-black/40 backdrop-blur-md text-white text-xs font-bold border border-white/10",
                    ),
                    rx.el.button(
                        rx.icon("heart", class_name="w-4 h-4 text-white"),
                        class_name="p-2 rounded-full bg-black/40 backdrop-blur-md hover:bg-pink-500 hover:text-white transition-colors border border-white/10 group-hover:scale-110",
                    ),
                    class_name="absolute top-4 left-4 right-4 flex justify-between items-start z-10 opacity-0 group-hover:opacity-100 transition-opacity duration-300",
                ),
                class_name=f"w-full aspect-square bg-gradient-to-br {listing['image_gradient']} group-hover:scale-110 transition-transform duration-700",
            ),
            rx.el.div(
                rx.el.button(
                    "Buy Now",
                    class_name="flex-1 py-3 bg-white text-black font-bold text-sm rounded hover:bg-[#56E1F6] transition-colors shadow-lg",
                ),
                rx.el.button(
                    "View",
                    class_name="px-4 py-3 bg-black/60 backdrop-blur-md text-white font-bold text-sm rounded border border-white/20 hover:bg-black/80 transition-colors",
                ),
                class_name="absolute bottom-4 left-4 right-4 flex gap-2 translate-y-4 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300 delay-75",
            ),
            class_name="relative overflow-hidden",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    listing["title"],
                    class_name="text-lg font-bold text-white mb-1 truncate group-hover:text-[#56E1F6] transition-colors",
                ),
                rx.el.p(
                    listing["artist"],
                    class_name="text-sm text-gray-400 font-medium mb-4",
                ),
                class_name="mb-4 border-b border-white/5 pb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Price",
                        class_name="text-xs text-gray-500 uppercase font-bold mb-1",
                    ),
                    rx.el.div(
                        rx.icon("gem", class_name="w-3 h-3 text-[#56E1F6] mr-1.5"),
                        rx.el.span(
                            f"{listing['price']} ETH",
                            class_name="text-sm font-bold text-white",
                        ),
                        class_name="flex items-center",
                    ),
                ),
                rx.el.div(
                    rx.el.p(
                        "Ending in",
                        class_name="text-xs text-gray-500 uppercase font-bold mb-1 text-right",
                    ),
                    rx.el.p(
                        listing["ends_in"],
                        class_name="text-sm font-bold text-gray-300 text-right font-mono",
                    ),
                ),
                class_name="flex justify-between items-end",
            ),
            class_name="p-5 bg-[#1a1a1e] group-hover:bg-[#202025] transition-colors duration-300",
        ),
        class_name="group rounded-2xl overflow-hidden border border-white/5 hover:border-[#56E1F6]/30 hover:shadow-[0_0_30px_rgba(86,225,246,0.1)] hover:-translate-y-2 transition-all duration-300 bg-[#1a1a1e]",
    )


def marketplace_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Explore Marketplace",
                    class_name="text-3xl md:text-4xl font-bold text-white",
                ),
                rx.el.p(
                    "Browse the largest collection of unique NFTs",
                    class_name="text-gray-400 mt-2",
                ),
                class_name="mb-10",
            ),
            rx.el.div(
                rx.el.div(
                    rx.foreach(NftState.categories, category_tab),
                    class_name="flex gap-3 overflow-x-auto pb-2 custom-scrollbar no-scrollbar flex-1",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "search",
                            class_name="w-4 h-4 text-gray-400 absolute left-4 top-1/2 -translate-y-1/2",
                        ),
                        rx.el.input(
                            placeholder="Search items...",
                            on_change=NftState.set_search_query,
                            class_name="bg-white/5 border border-white/10 rounded-full py-2.5 pl-11 pr-4 text-sm text-white placeholder-gray-500 focus:outline-none focus:border-[#56E1F6]/50 focus:ring-1 focus:ring-[#56E1F6]/50 w-full md:w-64 transition-all",
                        ),
                        class_name="relative",
                    ),
                    rx.el.div(
                        rx.el.select(
                            rx.foreach(
                                NftState.sort_options,
                                lambda opt: rx.el.option(opt, value=opt),
                            ),
                            on_change=NftState.set_sort_option,
                            class_name="appearance-none bg-white/5 border border-white/10 rounded-full py-2.5 pl-4 pr-10 text-sm text-white font-medium focus:outline-none focus:border-[#56E1F6]/50 cursor-pointer",
                        ),
                        rx.icon(
                            "chevron-down",
                            class_name="w-4 h-4 text-gray-400 absolute right-4 top-1/2 -translate-y-1/2 pointer-events-none",
                        ),
                        class_name="relative",
                    ),
                    class_name="flex flex-col sm:flex-row gap-4 w-full md:w-auto",
                ),
                class_name="flex flex-col lg:flex-row justify-between items-start lg:items-center gap-6 mb-12",
            ),
            rx.el.div(
                rx.cond(
                    NftState.is_loading_marketplace,
                    rx.fragment(
                        skeleton_card(),
                        skeleton_card(),
                        skeleton_card(),
                        skeleton_card(),
                        skeleton_card(),
                        skeleton_card(),
                        skeleton_card(),
                        skeleton_card(),
                    ),
                    rx.foreach(NftState.filtered_listings, nft_card),
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 md:gap-8",
            ),
            rx.el.div(
                rx.el.button(
                    "Load More items",
                    class_name="px-8 py-3 rounded-lg border border-white/10 text-white font-bold text-sm hover:bg-white/5 hover:border-white/20 transition-all",
                ),
                class_name="flex justify-center mt-16",
            ),
            class_name="max-w-[1440px] mx-auto px-6 w-full",
        ),
        rx.window_event_listener(on_mount=NftState.simulate_loading),
        class_name="py-20 bg-[#0f0f10] relative border-t border-white/5",
    )