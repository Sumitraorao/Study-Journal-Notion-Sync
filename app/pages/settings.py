import reflex as rx
from app.components.nft_navbar import nft_navbar
from app.states.wallet_state import WalletState


def settings_page() -> rx.Component:
    return rx.el.div(
        nft_navbar(),
        rx.el.main(
            rx.cond(
                WalletState.is_connected,
                rx.el.div(
                    rx.el.div(
                        rx.el.h1(
                            "Account Settings",
                            class_name="text-3xl font-bold text-white mb-2",
                        ),
                        rx.el.p(
                            "Manage your profile and preferences.",
                            class_name="text-gray-400 mb-12",
                        ),
                        rx.el.form(
                            rx.el.div(
                                rx.el.label(
                                    "Profile Image",
                                    class_name="block text-sm font-bold text-gray-400 uppercase mb-4",
                                ),
                                rx.el.div(
                                    rx.image(
                                        src=WalletState.avatar,
                                        class_name="w-24 h-24 rounded-full border-2 border-white/10 bg-[#1a1a1e]",
                                    ),
                                    rx.el.div(
                                        rx.el.button(
                                            "Upload new picture",
                                            type="button",
                                            class_name="px-4 py-2 bg-white/5 hover:bg-white/10 text-white font-bold rounded-lg border border-white/5 transition-colors mb-2",
                                        ),
                                        rx.el.p(
                                            "JPG, GIF or PNG. Max size of 800K",
                                            class_name="text-xs text-gray-500",
                                        ),
                                        class_name="flex flex-col",
                                    ),
                                    class_name="flex items-center gap-6",
                                ),
                                class_name="mb-12 p-6 bg-[#1a1a1e] rounded-2xl border border-white/5",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.label(
                                        "Display Name",
                                        class_name="block text-sm font-bold text-gray-400 uppercase mb-2",
                                    ),
                                    rx.el.input(
                                        name="username",
                                        default_value=WalletState.username,
                                        class_name="w-full bg-[#1a1a1e] border border-white/10 rounded-xl px-4 py-3 text-white focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 outline-none transition-all",
                                    ),
                                    class_name="mb-6",
                                ),
                                rx.el.div(
                                    rx.el.label(
                                        "Email Address",
                                        class_name="block text-sm font-bold text-gray-400 uppercase mb-2",
                                    ),
                                    rx.el.input(
                                        name="email",
                                        type="email",
                                        default_value=WalletState.email,
                                        placeholder="Enter your email",
                                        class_name="w-full bg-[#1a1a1e] border border-white/10 rounded-xl px-4 py-3 text-white focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 outline-none transition-all",
                                    ),
                                    class_name="mb-6",
                                ),
                                rx.el.div(
                                    rx.el.label(
                                        "Bio",
                                        class_name="block text-sm font-bold text-gray-400 uppercase mb-2",
                                    ),
                                    rx.el.textarea(
                                        name="bio",
                                        default_value=WalletState.bio,
                                        rows=4,
                                        class_name="w-full bg-[#1a1a1e] border border-white/10 rounded-xl px-4 py-3 text-white focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 outline-none transition-all resize-none",
                                    ),
                                    class_name="mb-8",
                                ),
                                rx.el.h3(
                                    "Notifications",
                                    class_name="text-lg font-bold text-white mb-4 mt-8",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.p(
                                                "Item Sold",
                                                class_name="font-bold text-white",
                                            ),
                                            rx.el.p(
                                                "When someone purchased one of your items",
                                                class_name="text-sm text-gray-500",
                                            ),
                                        ),
                                        rx.el.input(
                                            type="checkbox",
                                            default_checked=True,
                                            class_name="w-5 h-5 rounded bg-white/5 border-white/10 text-cyan-500 focus:ring-cyan-500",
                                        ),
                                        class_name="flex justify-between items-center py-4 border-b border-white/5",
                                    ),
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.p(
                                                "Bid Activity",
                                                class_name="font-bold text-white",
                                            ),
                                            rx.el.p(
                                                "When someone bids on your items",
                                                class_name="text-sm text-gray-500",
                                            ),
                                        ),
                                        rx.el.input(
                                            type="checkbox",
                                            default_checked=True,
                                            class_name="w-5 h-5 rounded bg-white/5 border-white/10 text-cyan-500 focus:ring-cyan-500",
                                        ),
                                        class_name="flex justify-between items-center py-4 border-b border-white/5",
                                    ),
                                    class_name="mb-12",
                                ),
                                rx.el.button(
                                    "Save Changes",
                                    type="submit",
                                    class_name="px-8 py-3 bg-cyan-500 hover:bg-cyan-400 text-black font-bold rounded-xl transition-colors",
                                ),
                                class_name="max-w-2xl",
                            ),
                            on_submit=WalletState.update_settings,
                        ),
                    ),
                    class_name="max-w-[1440px] mx-auto px-6 py-28",
                ),
                rx.el.div(
                    rx.icon("shield-alert", class_name="w-16 h-16 text-gray-600 mb-6"),
                    rx.el.h2(
                        "Access Denied", class_name="text-3xl font-bold text-white mb-4"
                    ),
                    rx.el.p(
                        "Please connect your wallet to manage settings.",
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