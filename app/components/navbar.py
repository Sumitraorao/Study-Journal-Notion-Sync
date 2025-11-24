import reflex as rx


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Phase 1: UI Demo",
                    class_name="px-2 py-1 rounded text-[10px] font-medium bg-cyan-500/10 text-cyan-400 border border-cyan-500/20",
                ),
                class_name="flex items-center",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        "moon",
                        class_name="w-5 h-5 text-gray-400 hover:text-white transition-colors",
                    ),
                    class_name="p-2 rounded-full hover:bg-white/10 transition-colors",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="max-w-screen-2xl mx-auto w-full flex items-center justify-between",
        ),
        class_name="h-16 flex items-center px-8 border-b border-white/5 sticky top-0 bg-[#0f0f10]/80 backdrop-blur-md z-20",
    )