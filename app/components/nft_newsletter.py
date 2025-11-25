import reflex as rx
from app.states.nft_state import NftState


def floating_shape() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="absolute inset-0 bg-gradient-to-tr from-blue-600 to-purple-600 rounded-3xl blur-xl opacity-50 animate-pulse"
        ),
        rx.el.div(
            rx.el.div(
                class_name="absolute inset-0 bg-gradient-to-br from-[#56E1F6] to-[#4f46e5] rounded-3xl opacity-90"
            ),
            rx.el.div(
                class_name="absolute inset-0 bg-[url('/placeholder.svg')] opacity-20 mix-blend-overlay"
            ),
            class_name="relative w-48 h-48 md:w-64 md:h-64 transform rotate-12 hover:rotate-6 transition-transform duration-700 shadow-2xl shadow-cyan-500/20 rounded-3xl animate-bounce [animation-duration:3s]",
        ),
        class_name="relative flex items-center justify-center py-12",
    )


def newsletter_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(floating_shape(), class_name="flex-1 flex justify-center"),
            rx.el.div(
                rx.el.h2(
                    "Join our newsletter to get premium access to the finest NFT artworks trending right now.",
                    class_name="text-3xl md:text-4xl lg:text-5xl font-bold text-white mb-8 leading-tight",
                ),
                rx.el.div(
                    rx.el.input(
                        placeholder="Enter your e-mail here",
                        on_change=NftState.set_newsletter_email,
                        class_name="w-full bg-white/5 border border-white/10 rounded-lg px-6 py-4 text-white placeholder-gray-500 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 transition-all",
                        default_value=NftState.newsletter_email,
                    ),
                    rx.el.button(
                        "Subscribe",
                        on_click=NftState.subscribe_newsletter,
                        class_name="absolute right-2 top-2 bottom-2 px-6 bg-[#56E1F6] text-black font-bold rounded hover:bg-[#4CD0E5] hover:shadow-[0_0_15px_rgba(86,225,246,0.4)] transition-all duration-300",
                    ),
                    class_name="relative max-w-md w-full",
                ),
                class_name="flex-1 max-w-2xl",
            ),
            class_name="max-w-[1440px] mx-auto px-6 w-full flex flex-col lg:flex-row items-center gap-12 lg:gap-24",
        ),
        class_name="py-20 bg-[#0f0f10] border-t border-white/5",
    )