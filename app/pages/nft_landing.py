import reflex as rx
from app.components.nft_navbar import nft_navbar
from app.components.nft_hero import hero_section
from app.components.nft_creators import top_creators_section
from app.components.nft_newsletter import newsletter_section
from app.components.nft_marketplace import marketplace_section


def nft_landing() -> rx.Component:
    return rx.el.div(
        nft_navbar(),
        hero_section(),
        top_creators_section(),
        marketplace_section(),
        newsletter_section(),
        class_name="bg-[#0f0f10] min-h-screen text-gray-100 selection:bg-purple-500/30 font-['Inter']",
    )