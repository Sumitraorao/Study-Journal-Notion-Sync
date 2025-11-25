import reflex as rx
from app.components.nft_navbar import nft_navbar
from app.states.wallet_state import WalletState, Transaction
from app.components.nft_marketplace import nft_card


def stat_card(label: str, value: str, icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="w-6 h-6 text-cyan-400"),
            class_name="w-12 h-12 rounded-full bg-cyan-500/10 flex items-center justify-center mb-4",
        ),
        rx.el.p(label, class_name="text-gray-400 text-sm font-medium mb-1"),
        rx.el.h3(value, class_name="text-2xl font-bold text-white"),
        class_name="bg-[#1a1a1e] p-6 rounded-2xl border border-white/5 hover:border-cyan-500/20 transition-all",
    )


def profile_header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="h-48 w-full bg-gradient-to-r from-purple-600/20 to-blue-600/20 rounded-3xl mb-16"
        ),
        rx.el.div(
            rx.el.div(
                rx.image(
                    src=WalletState.avatar,
                    class_name="w-32 h-32 rounded-full border-4 border-[#0f0f10] bg-[#1a1a1e]",
                ),
                class_name="absolute -bottom-16 left-8",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        WalletState.username,
                        class_name="text-3xl font-bold text-white mb-1",
                    ),
                    rx.el.p(
                        WalletState.wallet_address,
                        class_name="text-cyan-400 font-mono text-sm bg-cyan-500/10 px-3 py-1 rounded-full w-fit",
                    ),
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon("share-2", class_name="w-4 h-4"),
                        class_name="p-3 rounded-full bg-white/5 hover:bg-white/10 text-white border border-white/10 transition-colors",
                    ),
                    rx.el.a(
                        rx.icon("settings", class_name="w-4 h-4"),
                        href="/settings",
                        class_name="p-3 rounded-full bg-white/5 hover:bg-white/10 text-white border border-white/10 transition-colors",
                    ),
                    class_name="flex gap-3",
                ),
                class_name="flex justify-between items-end pl-44 pr-8 pb-4",
            ),
            class_name="relative",
        ),
        rx.el.p(
            WalletState.bio,
            class_name="text-gray-400 mt-4 max-w-2xl leading-relaxed px-4",
        ),
        class_name="mb-12",
    )


def transaction_row(tx: Transaction) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.icon(
                    rx.cond(
                        tx["type"] == "Purchase", "arrow-up-right", "arrow-down-left"
                    ),
                    class_name="w-4 h-4 text-cyan-400 mr-3",
                ),
                rx.el.span(tx["type"], class_name="text-white font-medium"),
                class_name="flex items-center",
            ),
            class_name="py-4 px-4 border-b border-white/5",
        ),
        rx.el.td(
            rx.el.span(tx["item_name"], class_name="text-gray-300"),
            class_name="py-4 px-4 border-b border-white/5",
        ),
        rx.el.td(
            rx.el.span(f"{tx['price']} ETH", class_name="text-white font-bold"),
            class_name="py-4 px-4 border-b border-white/5",
        ),
        rx.el.td(
            rx.el.span(tx["date"], class_name="text-gray-500 text-sm"),
            class_name="py-4 px-4 border-b border-white/5",
        ),
        rx.el.td(
            rx.el.span(
                tx["status"],
                class_name=f"text-xs font-bold px-2 py-1 rounded-full bg-white/5 {rx.cond(tx['status'] == 'Completed', 'text-green-400', 'text-yellow-400')}",
            ),
            class_name="py-4 px-4 border-b border-white/5",
        ),
    )


def profile_tabs() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.foreach(
                ["Owned", "Created", "Favorited", "Activity"],
                lambda tab: rx.el.button(
                    tab,
                    on_click=lambda: WalletState.set_active_tab(tab.lower()),
                    class_name=rx.cond(
                        WalletState.active_tab == tab.lower(),
                        "px-6 py-3 text-white font-bold border-b-2 border-cyan-400 transition-colors",
                        "px-6 py-3 text-gray-500 font-medium hover:text-gray-300 transition-colors",
                    ),
                ),
            ),
            class_name="flex border-b border-white/10 mb-8 overflow-x-auto",
        ),
        rx.cond(
            WalletState.active_tab == "owned",
            rx.cond(
                WalletState.owned_nfts,
                rx.el.div(
                    rx.foreach(WalletState.owned_nfts, nft_card),
                    class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6",
                ),
                rx.el.div(
                    rx.icon("ghost", class_name="w-16 h-16 text-gray-600 mb-4"),
                    rx.el.p("No items found", class_name="text-gray-500 text-lg"),
                    class_name="flex flex-col items-center justify-center py-20 border border-dashed border-white/10 rounded-2xl",
                ),
            ),
        ),
        rx.cond(
            WalletState.active_tab == "activity",
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Type",
                            class_name="text-left text-xs font-bold text-gray-500 uppercase px-4 py-3 bg-white/5 rounded-l-lg",
                        ),
                        rx.el.th(
                            "Item",
                            class_name="text-left text-xs font-bold text-gray-500 uppercase px-4 py-3 bg-white/5",
                        ),
                        rx.el.th(
                            "Price",
                            class_name="text-left text-xs font-bold text-gray-500 uppercase px-4 py-3 bg-white/5",
                        ),
                        rx.el.th(
                            "Date",
                            class_name="text-left text-xs font-bold text-gray-500 uppercase px-4 py-3 bg-white/5",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="text-left text-xs font-bold text-gray-500 uppercase px-4 py-3 bg-white/5 rounded-r-lg",
                        ),
                    )
                ),
                rx.el.tbody(rx.foreach(WalletState.transactions, transaction_row)),
                class_name="w-full text-left border-collapse",
            ),
        ),
        class_name="min-h-[400px]",
    )


def profile_page() -> rx.Component:
    return rx.el.div(
        nft_navbar(),
        rx.el.main(
            rx.cond(
                WalletState.is_connected,
                rx.el.div(
                    profile_header(),
                    rx.el.div(
                        stat_card(
                            "Total Value", f"{WalletState.balance} ETH", "wallet"
                        ),
                        stat_card(
                            "Items Owned",
                            f"{WalletState.owned_nfts.length()}",
                            "layers",
                        ),
                        stat_card("Items Created", "0", "palette"),
                        class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12",
                    ),
                    profile_tabs(),
                    class_name="max-w-[1440px] mx-auto px-6 py-28",
                ),
                rx.el.div(
                    rx.icon("lock", class_name="w-16 h-16 text-gray-600 mb-6"),
                    rx.el.h2(
                        "Connect your wallet",
                        class_name="text-3xl font-bold text-white mb-4",
                    ),
                    rx.el.p(
                        "Please connect your wallet to view your profile.",
                        class_name="text-gray-400 mb-8",
                    ),
                    rx.el.button(
                        "Connect Wallet",
                        on_click=WalletState.toggle_modal,
                        class_name="px-8 py-3 rounded-full bg-gradient-to-r from-purple-600 to-pink-600 text-white font-bold hover:shadow-lg transition-all",
                    ),
                    class_name="min-h-[60vh] flex flex-col items-center justify-center pt-20",
                ),
            ),
            class_name="min-h-screen bg-[#0f0f10]",
        ),
        class_name="bg-[#0f0f10] min-h-screen font-['Inter']",
    )