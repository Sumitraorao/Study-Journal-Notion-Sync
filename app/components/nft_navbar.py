import reflex as rx
from app.states.wallet_state import WalletState
from app.components.wallet_modal import wallet_modal


def nft_navbar() -> rx.Component:
    return rx.el.nav(
        wallet_modal(),
        rx.el.div(
            rx.el.a(
                rx.icon("rocket", class_name="w-8 h-8 text-purple-500 mr-2"),
                rx.el.span(
                    "NFTrade",
                    class_name="text-2xl font-bold text-white tracking-tighter",
                ),
                href="/",
                class_name="flex items-center cursor-pointer group",
            ),
            rx.el.div(
                rx.cond(
                    WalletState.is_connected,
                    rx.el.div(
                        rx.el.a(
                            "Create",
                            href="/create",
                            class_name="text-sm font-bold text-gray-300 hover:text-white transition-colors mr-6",
                        ),
                        rx.el.div(
                            rx.el.button(
                                rx.image(
                                    src=WalletState.avatar,
                                    class_name="w-8 h-8 rounded-full border border-white/10",
                                ),
                                rx.el.span(
                                    WalletState.wallet_address,
                                    class_name="text-sm font-medium text-white ml-2 max-w-[100px] truncate",
                                ),
                                rx.icon(
                                    "chevron-down",
                                    class_name="w-4 h-4 text-gray-400 ml-2",
                                ),
                                class_name="flex items-center bg-white/5 hover:bg-white/10 px-3 py-1.5 rounded-full transition-colors border border-white/5",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.p(
                                        "Balance",
                                        class_name="text-xs text-gray-500 uppercase font-bold mb-1",
                                    ),
                                    rx.el.p(
                                        f"{WalletState.balance} ETH",
                                        class_name="text-lg font-bold text-white mb-4",
                                    ),
                                    rx.el.a(
                                        rx.el.div(
                                            rx.icon("user", class_name="w-4 h-4 mr-2"),
                                            "My Profile",
                                            class_name="flex items-center",
                                        ),
                                        href="/profile",
                                        class_name="block w-full text-left text-sm text-gray-300 hover:text-white hover:bg-white/5 py-2 px-3 rounded transition-colors mb-1",
                                    ),
                                    rx.el.a(
                                        rx.el.div(
                                            rx.icon(
                                                "settings", class_name="w-4 h-4 mr-2"
                                            ),
                                            "Settings",
                                            class_name="flex items-center",
                                        ),
                                        href="/settings",
                                        class_name="block w-full text-left text-sm text-gray-300 hover:text-white hover:bg-white/5 py-2 px-3 rounded transition-colors mb-1",
                                    ),
                                    rx.el.button(
                                        rx.el.div(
                                            rx.icon(
                                                "log-out", class_name="w-4 h-4 mr-2"
                                            ),
                                            "Disconnect",
                                            class_name="flex items-center",
                                        ),
                                        on_click=WalletState.disconnect_wallet,
                                        class_name="block w-full text-left text-sm text-red-400 hover:text-red-300 hover:bg-red-500/10 py-2 px-3 rounded transition-colors",
                                    ),
                                    class_name="absolute top-full right-0 mt-2 w-64 bg-[#18181b] border border-white/10 rounded-xl p-4 shadow-2xl opacity-0 group-hover:opacity-100 invisible group-hover:visible transition-all transform origin-top-right z-50",
                                ),
                                class_name="relative group",
                            ),
                            class_name="flex items-center gap-4",
                        ),
                        class_name="flex items-center",
                    ),
                    rx.el.button(
                        "Connect wallet",
                        on_click=WalletState.toggle_modal,
                        class_name="px-6 py-2.5 rounded-full bg-gradient-to-r from-purple-600 to-pink-600 text-white font-medium hover:shadow-lg hover:shadow-purple-500/30 transition-all transform hover:-translate-y-0.5 active:translate-y-0 text-sm",
                    ),
                ),
                class_name="flex items-center",
            ),
            class_name="max-w-7xl mx-auto px-6 h-20 flex justify-between items-center",
        ),
        class_name="w-full fixed top-0 z-50 bg-[#0f0f10]/80 backdrop-blur-md border-b border-white/5",
    )