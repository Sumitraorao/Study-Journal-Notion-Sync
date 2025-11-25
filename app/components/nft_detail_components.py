import reflex as rx
from app.states.nft_detail_state import NFTDetailState, Bid, Property
from app.states.nft_state import NftState
from app.components.nft_marketplace import nft_card


def detail_header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                NFTDetailState.title,
                class_name="text-4xl md:text-5xl font-black text-white mb-4 tracking-tight",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("share-2", class_name="w-5 h-5"),
                    on_click=NFTDetailState.copy_link,
                    class_name="p-3 rounded-full bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white transition-all border border-white/5",
                    title="Share",
                ),
                rx.el.button(
                    rx.icon("send_horizontal", class_name="w-5 h-5"),
                    class_name="p-3 rounded-full bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white transition-all border border-white/5",
                ),
                class_name="flex gap-3",
            ),
            class_name="flex justify-between items-start",
        ),
        rx.el.div(
            rx.el.span("Owned by", class_name="text-gray-500 mr-2"),
            rx.el.span(
                NFTDetailState.owner_name, class_name="text-cyan-400 font-medium mr-6"
            ),
            rx.el.span("Created by", class_name="text-gray-500 mr-2"),
            rx.el.span(
                NFTDetailState.creator_name, class_name="text-purple-400 font-medium"
            ),
            class_name="flex items-center text-sm mb-8",
        ),
        class_name="mb-6",
    )


def price_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p("Current price", class_name="text-gray-500 text-sm mb-1"),
            rx.el.div(
                rx.el.h2(
                    f"{NFTDetailState.current_price} ETH",
                    class_name="text-3xl font-bold text-white",
                ),
                rx.el.span("$12,450.55", class_name="text-gray-500 text-sm ml-3 mt-2"),
                class_name="flex items-baseline mb-6",
            ),
            rx.el.div(
                rx.el.button(
                    rx.cond(
                        NFTDetailState.is_placing_bid,
                        rx.spinner(size="1", class_name="text-black mx-auto"),
                        "Place a bid",
                    ),
                    disabled=NFTDetailState.is_placing_bid,
                    on_click=rx.set_focus("bid_input"),
                    class_name="w-full py-4 bg-[#56E1F6] hover:bg-[#4CD0E5] text-black font-bold rounded-xl transition-all shadow-[0_0_20px_rgba(86,225,246,0.2)] active:scale-95 mb-3",
                ),
                rx.el.button(
                    "Make offer",
                    class_name="w-full py-4 bg-white/5 hover:bg-white/10 text-white font-bold rounded-xl transition-all border border-white/10 hover:border-white/20",
                ),
                class_name="space-y-3",
            ),
            class_name="bg-[#202023] p-6 rounded-2xl border border-white/5",
        ),
        rx.el.div(
            rx.el.p("Auction ends in", class_name="text-gray-500 text-sm mb-2"),
            rx.el.div(
                rx.el.div(
                    rx.el.span("01", class_name="text-2xl font-bold text-white"),
                    rx.el.span("Days", class_name="text-xs text-gray-500 block"),
                    class_name="bg-black/20 p-3 rounded-lg text-center min-w-[70px]",
                ),
                rx.el.div(
                    rx.el.span("11", class_name="text-2xl font-bold text-white"),
                    rx.el.span("Hours", class_name="text-xs text-gray-500 block"),
                    class_name="bg-black/20 p-3 rounded-lg text-center min-w-[70px]",
                ),
                rx.el.div(
                    rx.el.span("36", class_name="text-2xl font-bold text-white"),
                    rx.el.span("Mins", class_name="text-xs text-gray-500 block"),
                    class_name="bg-black/20 p-3 rounded-lg text-center min-w-[70px]",
                ),
                rx.el.div(
                    rx.el.span("42", class_name="text-2xl font-bold text-white"),
                    rx.el.span("Secs", class_name="text-xs text-gray-500 block"),
                    class_name="bg-black/20 p-3 rounded-lg text-center min-w-[70px]",
                ),
                class_name="flex gap-3",
            ),
            class_name="mt-6",
        ),
        class_name="bg-[#1a1a1e] p-6 rounded-3xl border border-white/5",
    )


def bid_input_section() -> rx.Component:
    return rx.el.div(
        rx.el.label(
            "Your bid",
            class_name="text-sm font-bold text-gray-400 uppercase mb-2 block",
        ),
        rx.el.div(
            rx.el.input(
                id="bid_input",
                type="number",
                placeholder="Enter bid amount...",
                on_change=NFTDetailState.set_bid_amount,
                class_name="w-full bg-black/20 border border-white/10 rounded-xl py-3 px-4 text-white focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 outline-none transition-all",
                default_value=NFTDetailState.bid_amount,
            ),
            rx.el.span(
                "ETH",
                class_name="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 font-bold",
            ),
            class_name="relative mb-4",
        ),
        rx.el.div(
            rx.el.button(
                "Confirm Bid",
                on_click=NFTDetailState.place_bid,
                disabled=NFTDetailState.is_placing_bid,
                class_name="px-6 py-2 bg-gradient-to-r from-purple-600 to-blue-600 rounded-lg text-white font-bold text-sm hover:shadow-lg hover:shadow-purple-500/20 transition-all disabled:opacity-50 disabled:cursor-not-allowed",
            ),
            class_name="flex justify-end",
        ),
        class_name="mt-8 pt-8 border-t border-white/5",
    )


def history_graph() -> rx.Component:
    return rx.el.div(
        rx.recharts.line_chart(
            rx.recharts.cartesian_grid(
                stroke_dasharray="3 3", vertical=False, stroke="#333"
            ),
            rx.recharts.x_axis(
                data_key="date",
                stroke="#666",
                font_size=12,
                tick_line=False,
                axis_line=False,
            ),
            rx.recharts.y_axis(
                stroke="#666",
                font_size=12,
                tick_line=False,
                axis_line=False,
                unit=" ETH",
            ),
            rx.recharts.tooltip(
                content_style={
                    "backgroundColor": "#1a1a1e",
                    "borderColor": "#333",
                    "borderRadius": "8px",
                },
                item_style={"color": "#fff"},
            ),
            rx.recharts.line(
                data_key="price",
                stroke="#56E1F6",
                stroke_width=3,
                dot={"fill": "#56E1F6", "r": 4, "strokeWidth": 2, "stroke": "#fff"},
                active_dot={"r": 6},
                type_="monotone",
            ),
            data=NFTDetailState.price_history,
            height=250,
            width="100%",
        ),
        class_name="w-full h-[250px] mt-4",
    )


def property_card(prop: Property) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            prop["type"], class_name="text-xs text-cyan-400 uppercase font-bold mb-1"
        ),
        rx.el.p(prop["value"], class_name="text-white font-medium text-lg truncate"),
        rx.el.p(
            f"{prop['rarity']} have this trait", class_name="text-xs text-gray-500 mt-2"
        ),
        class_name="bg-[#202023] p-4 rounded-xl border border-cyan-500/20 hover:border-cyan-500/50 transition-all hover:bg-cyan-500/5 cursor-default",
    )


def bid_row(bid: Bid) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=f"https://api.dicebear.com/9.x/notionists/svg?seed={bid['user']}",
                class_name="w-10 h-10 rounded-full bg-white/10",
            ),
            rx.el.div(
                rx.el.p(
                    rx.el.span(
                        bid["user"],
                        class_name="text-white font-bold hover:text-cyan-400 cursor-pointer transition-colors",
                    ),
                    " placed a bid",
                    class_name="text-gray-400 text-sm",
                ),
                rx.el.p(bid["time"], class_name="text-xs text-gray-600"),
                class_name="ml-3",
            ),
            class_name="flex items-center",
        ),
        rx.el.div(
            rx.icon("gem", class_name="w-3 h-3 text-cyan-400 mr-1"),
            rx.el.span(f"{bid['price']} ETH", class_name="text-white font-bold"),
            class_name="flex items-center bg-white/5 px-3 py-1.5 rounded-lg border border-white/5",
        ),
        class_name="flex justify-between items-center py-3 border-b border-white/5 last:border-0 animate-fade-in",
    )


def tab_button(label: str, value: str) -> rx.Component:
    is_active = NFTDetailState.active_tab == value
    return rx.el.button(
        label,
        on_click=lambda: NFTDetailState.set_active_tab(value),
        class_name=rx.cond(
            is_active,
            "px-6 py-3 text-white font-bold border-b-2 border-cyan-400 transition-colors",
            "px-6 py-3 text-gray-500 font-medium hover:text-gray-300 transition-colors",
        ),
    )


def details_tabs() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            tab_button("Bid History", "history"),
            tab_button("Properties", "properties"),
            tab_button("Price History", "chart"),
            class_name="flex border-b border-white/10 mb-6 overflow-x-auto",
        ),
        rx.el.div(
            rx.cond(
                NFTDetailState.active_tab == "history",
                rx.el.div(
                    rx.foreach(NFTDetailState.bids, bid_row),
                    class_name="max-h-[400px] overflow-y-auto pr-2 custom-scrollbar",
                ),
            ),
            rx.cond(
                NFTDetailState.active_tab == "properties",
                rx.el.div(
                    rx.foreach(NFTDetailState.properties, property_card),
                    class_name="grid grid-cols-2 sm:grid-cols-3 gap-4",
                ),
            ),
            rx.cond(NFTDetailState.active_tab == "chart", history_graph()),
            class_name="min-h-[300px]",
        ),
        class_name="mt-12",
    )


def related_carousel() -> rx.Component:
    return rx.el.section(
        rx.el.h3(
            "More from this collection", class_name="text-2xl font-bold text-white mb-8"
        ),
        rx.el.div(
            rx.foreach(NftState.listings[:4], nft_card),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6",
        ),
        class_name="py-20 border-t border-white/5",
    )