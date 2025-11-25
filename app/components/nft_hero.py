import reflex as rx


def stat_counter(count: str, label: str) -> rx.Component:
    return rx.el.div(
        rx.el.h3(count, class_name="text-3xl md:text-4xl font-bold text-white"),
        rx.el.p(label, class_name="text-gray-400 text-sm font-medium mt-1"),
        class_name="flex flex-col",
    )


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            class_name="absolute top-[-10%] left-[-10%] w-[40rem] h-[40rem] bg-purple-600/20 rounded-full blur-[120px] -z-10 animate-pulse duration-[5000ms]"
        ),
        rx.el.div(
            class_name="absolute top-[20%] right-[-5%] w-[35rem] h-[35rem] bg-pink-600/10 rounded-full blur-[100px] -z-10 animate-pulse delay-1000 duration-[7000ms]"
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Discover, collect and sell unique NFT artworks",
                        class_name="text-6xl md:text-7xl lg:text-8xl font-black text-white leading-[1.1] mb-8 tracking-tight",
                    ),
                    rx.el.p(
                        "The world's largest digital marketplace for crypto collectibles and non-fungible tokens (NFTs). Buy, sell, and discover exclusive digital assets.",
                        class_name="text-gray-400 text-xl md:text-2xl mb-12 max-w-2xl leading-relaxed",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Start collecting",
                            class_name="px-8 py-4 rounded-lg bg-[#56E1F6] text-black font-bold hover:bg-[#4CD0E5] hover:shadow-[0_0_20px_rgba(86,225,246,0.4)] hover:-translate-y-1 transition-all duration-300 transform active:scale-95 text-lg",
                        ),
                        rx.el.button(
                            "Create NFT",
                            class_name="px-8 py-4 rounded-lg bg-transparent text-white font-bold border border-white/20 hover:bg-white/5 hover:border-white/40 hover:-translate-y-1 transition-all duration-300 transform active:scale-95 text-lg",
                        ),
                        class_name="flex flex-col sm:flex-row gap-4 mb-20",
                    ),
                    rx.el.div(
                        stat_counter("7K+", "Artworks"),
                        rx.el.div(class_name="w-px h-12 bg-white/10"),
                        stat_counter("1K+", "Artists"),
                        rx.el.div(class_name="w-px h-12 bg-white/10"),
                        stat_counter("250K+", "Active users"),
                        class_name="flex gap-8 items-center",
                    ),
                    class_name="flex-1 flex flex-col justify-center z-10",
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "rocket",
                                    class_name="w-48 h-48 text-orange-400 drop-shadow-[0_10px_20px_rgba(0,0,0,0.5)] transform transition-transform duration-700 group-hover:scale-110 group-hover:-rotate-12",
                                ),
                                class_name="absolute inset-0 flex items-center justify-center bg-[#1a1a1e]",
                            ),
                            class_name="w-full h-[360px] relative overflow-hidden",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.div(
                                    rx.el.p(
                                        "Current bid",
                                        class_name="text-xs text-gray-500 font-bold uppercase tracking-wider mb-1",
                                    ),
                                    rx.el.p(
                                        "4.1 ETH",
                                        class_name="text-2xl font-bold text-gray-900",
                                    ),
                                ),
                                rx.el.div(
                                    rx.el.p(
                                        "Remaining time",
                                        class_name="text-xs text-gray-500 font-bold uppercase tracking-wider mb-1 text-right",
                                    ),
                                    rx.el.p(
                                        "1d 11h 36m 42s",
                                        class_name="text-xl font-bold text-gray-900 font-mono text-right",
                                    ),
                                ),
                                class_name="flex justify-between items-end mb-8",
                            ),
                            rx.el.div(
                                rx.el.button(
                                    "Buy now",
                                    class_name="flex-1 bg-[#1a1a1e] text-white font-bold py-3.5 px-6 rounded hover:bg-black hover:shadow-lg transition-all duration-200 active:transform active:scale-95",
                                ),
                                rx.el.button(
                                    "View artwork",
                                    class_name="flex-1 bg-transparent border border-gray-300 text-gray-900 font-bold py-3.5 px-6 rounded hover:border-gray-900 hover:bg-gray-50 transition-all duration-200",
                                ),
                                class_name="flex gap-4",
                            ),
                            class_name="p-6 bg-white",
                        ),
                        class_name="w-full max-w-[400px] bg-white rounded-none overflow-hidden shadow-2xl transform transition-all duration-500 hover:-translate-y-2 hover:shadow-[0_30px_60px_rgba(86,225,246,0.2)]",
                    ),
                    rx.el.div(
                        class_name="absolute -inset-4 bg-gradient-to-r from-purple-600/20 to-blue-600/20 rounded-xl blur-2xl -z-10 opacity-0 group-hover:opacity-100 transition-opacity duration-500"
                    ),
                    class_name="relative group perspective-1000",
                ),
                class_name="flex-1 flex items-center justify-center lg:justify-end mt-12 lg:mt-0 z-10",
            ),
            class_name="max-w-[1440px] mx-auto px-6 w-full flex flex-col lg:flex-row gap-12 lg:gap-24 items-center justify-between",
        ),
        class_name="w-full min-h-screen relative overflow-hidden bg-[#0f0f10] flex items-center justify-center pt-32 pb-20",
    )