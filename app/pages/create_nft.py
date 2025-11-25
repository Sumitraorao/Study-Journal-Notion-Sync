import reflex as rx
from app.components.nft_navbar import nft_navbar
from app.states.create_nft_state import CreateNftState, Property
from app.states.wallet_state import WalletState


def property_input_row(prop: Property, index: int) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(prop["type"], class_name="text-gray-400 text-sm font-medium"),
            rx.el.p(prop["value"], class_name="text-white font-bold"),
            class_name="flex-1 bg-white/5 px-4 py-2 rounded-lg border border-white/5",
        ),
        rx.el.button(
            rx.icon("trash-2", class_name="w-4 h-4 text-red-400"),
            on_click=lambda: CreateNftState.remove_property(index),
            class_name="p-2 hover:bg-red-500/10 rounded-lg transition-colors",
        ),
        class_name="flex items-center gap-2 animate-fade-in",
    )


def success_modal() -> rx.Component:
    return rx.cond(
        CreateNftState.show_success_modal,
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "check_check",
                        class_name="w-20 h-20 text-green-500 mb-6 animate-bounce",
                    ),
                    rx.el.h2(
                        "NFT Created Successfully!",
                        class_name="text-2xl font-bold text-white mb-2",
                    ),
                    rx.el.p(
                        "Your artwork has been minted and listed on the marketplace.",
                        class_name="text-gray-400 mb-8 text-center",
                    ),
                    rx.el.button(
                        "View Listing",
                        on_click=CreateNftState.close_success_modal,
                        class_name="w-full py-3 bg-green-500 hover:bg-green-600 text-white font-bold rounded-xl transition-colors",
                    ),
                    class_name="bg-[#18181b] border border-white/10 rounded-2xl p-8 max-w-md w-full flex flex-col items-center shadow-2xl",
                ),
                class_name="fixed inset-0 z-50 flex items-center justify-center p-4",
            ),
            rx.el.div(class_name="fixed inset-0 bg-black/80 backdrop-blur-sm z-40"),
            class_name="relative z-50",
        ),
    )


def create_nft_page() -> rx.Component:
    return rx.el.div(
        nft_navbar(),
        success_modal(),
        rx.el.main(
            rx.cond(
                WalletState.is_connected,
                rx.el.div(
                    rx.el.div(
                        rx.el.h1(
                            "Create New NFT",
                            class_name="text-4xl font-bold text-white mb-4",
                        ),
                        rx.el.p(
                            "Mint your digital artwork and list it on the marketplace.",
                            class_name="text-gray-400 mb-12",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Upload File",
                                    class_name="block text-sm font-bold text-gray-400 uppercase mb-4",
                                ),
                                rx.upload.root(
                                    rx.el.div(
                                        rx.cond(
                                            CreateNftState.uploaded_file_name,
                                            rx.el.div(
                                                rx.image(
                                                    src=rx.get_upload_url(
                                                        CreateNftState.uploaded_file_name
                                                    ),
                                                    class_name="w-full h-full object-cover rounded-xl",
                                                ),
                                                rx.el.div(
                                                    rx.icon(
                                                        "check_check",
                                                        class_name="w-8 h-8 text-green-400",
                                                    ),
                                                    class_name="absolute top-4 right-4 bg-black/50 rounded-full backdrop-blur-sm",
                                                ),
                                                class_name="w-full h-full relative",
                                            ),
                                            rx.el.div(
                                                rx.icon(
                                                    "cloud_upload",
                                                    class_name="w-16 h-16 text-gray-500 mb-4",
                                                ),
                                                rx.el.p(
                                                    "PNG, JPG, GIF, WEBP up to 10MB",
                                                    class_name="text-gray-500 text-center mb-4",
                                                ),
                                                rx.el.button(
                                                    "Choose File",
                                                    class_name="px-6 py-2 bg-white/10 hover:bg-white/20 text-white rounded-lg font-bold transition-colors",
                                                ),
                                                class_name="flex flex-col items-center justify-center",
                                            ),
                                        ),
                                        class_name="w-full aspect-square rounded-2xl border-2 border-dashed border-white/10 bg-[#1a1a1e] hover:bg-[#202025] transition-colors flex items-center justify-center p-4 relative overflow-hidden",
                                    ),
                                    id="upload_nft",
                                    accept={
                                        "image/png": [".png"],
                                        "image/jpeg": [".jpg", ".jpeg"],
                                        "image/gif": [".gif"],
                                        "image/webp": [".webp"],
                                    },
                                    multiple=False,
                                    max_files=1,
                                    class_name="w-full",
                                ),
                                rx.el.button(
                                    rx.cond(
                                        CreateNftState.is_uploading,
                                        rx.el.span(
                                            f"Uploading... {CreateNftState.upload_progress}%",
                                            class_name="animate-pulse",
                                        ),
                                        "Confirm Upload",
                                    ),
                                    type="button",
                                    disabled=CreateNftState.is_uploading,
                                    on_click=CreateNftState.handle_upload(
                                        rx.upload_files(upload_id="upload_nft")
                                    ),
                                    class_name="mt-4 w-full py-3 bg-white/5 hover:bg-white/10 text-white font-bold rounded-xl border border-white/5 transition-all disabled:opacity-50",
                                ),
                                class_name="lg:col-span-4",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.label(
                                        "Display Name",
                                        class_name="block text-sm font-bold text-gray-400 uppercase mb-2",
                                    ),
                                    rx.el.input(
                                        placeholder="e.g. Cosmic Dreams #001",
                                        on_change=CreateNftState.set_name,
                                        class_name="w-full bg-[#1a1a1e] border border-white/10 rounded-xl px-4 py-3 text-white focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 outline-none transition-all",
                                        default_value=CreateNftState.name,
                                    ),
                                    class_name="mb-6",
                                ),
                                rx.el.div(
                                    rx.el.label(
                                        "Description",
                                        class_name="block text-sm font-bold text-gray-400 uppercase mb-2",
                                    ),
                                    rx.el.textarea(
                                        placeholder="Tell the story behind your artwork...",
                                        rows=4,
                                        on_change=CreateNftState.set_description,
                                        class_name="w-full bg-[#1a1a1e] border border-white/10 rounded-xl px-4 py-3 text-white focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 outline-none transition-all resize-none",
                                        default_value=CreateNftState.description,
                                    ),
                                    class_name="mb-6",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.label(
                                            "Price (ETH)",
                                            class_name="block text-sm font-bold text-gray-400 uppercase mb-2",
                                        ),
                                        rx.el.input(
                                            type="number",
                                            placeholder="0.00",
                                            step="0.01",
                                            on_change=CreateNftState.set_price,
                                            class_name="w-full bg-[#1a1a1e] border border-white/10 rounded-xl px-4 py-3 text-white focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 outline-none transition-all",
                                            default_value=CreateNftState.price,
                                        ),
                                    ),
                                    rx.el.div(
                                        rx.el.label(
                                            "Category",
                                            class_name="block text-sm font-bold text-gray-400 uppercase mb-2",
                                        ),
                                        rx.el.select(
                                            rx.el.option("Art", value="Art"),
                                            rx.el.option(
                                                "Photography", value="Photography"
                                            ),
                                            rx.el.option("Games", value="Games"),
                                            rx.el.option("Music", value="Music"),
                                            on_change=CreateNftState.set_category,
                                            class_name="w-full bg-[#1a1a1e] border border-white/10 rounded-xl px-4 py-3 text-white focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 outline-none transition-all appearance-none",
                                        ),
                                    ),
                                    class_name="grid grid-cols-2 gap-4 mb-8",
                                ),
                                rx.el.div(
                                    rx.el.label(
                                        "Properties",
                                        class_name="block text-sm font-bold text-gray-400 uppercase mb-4",
                                    ),
                                    rx.el.div(
                                        rx.foreach(
                                            CreateNftState.properties,
                                            lambda p, i: property_input_row(p, i),
                                        ),
                                        class_name="space-y-3 mb-4",
                                    ),
                                    rx.el.div(
                                        rx.el.input(
                                            placeholder="Type (e.g. Color)",
                                            on_change=CreateNftState.set_new_prop_type,
                                            class_name="bg-[#1a1a1e] border border-white/10 rounded-lg px-3 py-2 text-sm text-white focus:border-cyan-500 outline-none",
                                            default_value=CreateNftState.new_prop_type,
                                        ),
                                        rx.el.input(
                                            placeholder="Value (e.g. Blue)",
                                            on_change=CreateNftState.set_new_prop_value,
                                            class_name="bg-[#1a1a1e] border border-white/10 rounded-lg px-3 py-2 text-sm text-white focus:border-cyan-500 outline-none",
                                            default_value=CreateNftState.new_prop_value,
                                        ),
                                        rx.el.button(
                                            rx.icon("plus", class_name="w-4 h-4"),
                                            on_click=CreateNftState.add_property,
                                            class_name="p-2 bg-white/10 hover:bg-white/20 text-white rounded-lg transition-colors",
                                        ),
                                        class_name="grid grid-cols-[1fr_1fr_auto] gap-2",
                                    ),
                                    class_name="bg-[#1a1a1e]/50 border border-white/5 rounded-xl p-6 mb-8",
                                ),
                                rx.el.button(
                                    rx.cond(
                                        CreateNftState.is_minting,
                                        rx.el.div(
                                            rx.spinner(
                                                size="2", class_name="text-black mr-2"
                                            ),
                                            "Minting...",
                                        ),
                                        "Mint NFT",
                                    ),
                                    on_click=CreateNftState.mint_nft,
                                    disabled=CreateNftState.is_minting,
                                    class_name="w-full py-4 bg-[#56E1F6] hover:bg-[#4CD0E5] text-black font-bold text-lg rounded-xl shadow-[0_0_20px_rgba(86,225,246,0.3)] transition-all hover:-translate-y-1 disabled:opacity-50 disabled:hover:translate-y-0 flex items-center justify-center",
                                ),
                                class_name="lg:col-span-8",
                            ),
                            class_name="grid grid-cols-1 lg:grid-cols-12 gap-12",
                        ),
                    ),
                    class_name="max-w-[1440px] mx-auto px-6 py-28",
                ),
                rx.el.div(
                    rx.icon("wallet", class_name="w-16 h-16 text-gray-600 mb-6"),
                    rx.el.h2(
                        "Connect your wallet",
                        class_name="text-3xl font-bold text-white mb-4",
                    ),
                    rx.el.p(
                        "You need to connect your wallet to create NFTs.",
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