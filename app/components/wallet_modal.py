import reflex as rx
from app.states.wallet_state import WalletState


def provider_button(name: str, icon_url: str, bg_color: str) -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.image(src=icon_url, class_name="w-8 h-8 object-contain"),
            class_name=f"w-12 h-12 rounded-full {bg_color} flex items-center justify-center mb-2",
        ),
        rx.el.span(name, class_name="font-bold text-white"),
        on_click=lambda: WalletState.connect_wallet(name),
        disabled=WalletState.is_connecting,
        class_name="flex flex-col items-center justify-center p-4 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 transition-all hover:scale-105 active:scale-95",
    )


def wallet_modal() -> rx.Component:
    return rx.cond(
        WalletState.show_modal,
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Connect Wallet", class_name="text-2xl font-bold text-white"
                        ),
                        rx.el.button(
                            rx.icon("x", class_name="w-6 h-6 text-gray-400"),
                            on_click=WalletState.toggle_modal,
                            class_name="p-2 hover:bg-white/10 rounded-full transition-colors",
                        ),
                        class_name="flex justify-between items-center mb-8",
                    ),
                    rx.el.p(
                        "Choose a wallet you want to connect. There are several wallet providers.",
                        class_name="text-gray-400 mb-8",
                    ),
                    rx.cond(
                        WalletState.is_connecting,
                        rx.el.div(
                            rx.spinner(size="3", class_name="text-cyan-400 mb-4"),
                            rx.el.p(
                                "Connecting to wallet...",
                                class_name="text-white animate-pulse",
                            ),
                            class_name="flex flex-col items-center justify-center py-12",
                        ),
                        rx.el.div(
                            provider_button(
                                "MetaMask", "/metamask-logo.svg", "bg-orange-100"
                            ),
                            provider_button(
                                "Coinbase", "/coinbase-logo.svg", "bg-blue-100"
                            ),
                            provider_button(
                                "WalletConnect",
                                "/walletconnect-logo.svg",
                                "bg-blue-500",
                            ),
                            class_name="grid grid-cols-3 gap-4",
                        ),
                    ),
                    class_name="bg-[#18181b] border border-white/10 rounded-2xl p-8 max-w-md w-full shadow-2xl transform transition-all",
                ),
                class_name="fixed inset-0 z-50 flex items-center justify-center p-4 animate-fade-in",
            ),
            rx.el.div(
                class_name="fixed inset-0 bg-black/80 backdrop-blur-sm z-40",
                on_click=WalletState.toggle_modal,
            ),
            class_name="relative z-50",
        ),
    )