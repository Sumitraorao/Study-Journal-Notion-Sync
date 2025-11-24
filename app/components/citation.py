import reflex as rx


def citation_card(index: int, source: str) -> rx.Component:
    domain = rx.cond(source.contains("//"), source.split("/")[2], source)
    return rx.el.a(
        rx.el.div(
            rx.el.span(
                f"{index + 1}",
                class_name="text-[10px] font-bold text-gray-500 bg-gray-200/10 px-1.5 py-0.5 rounded-md mr-2",
            ),
            rx.el.div(
                rx.el.span(
                    domain,
                    class_name="text-xs font-medium text-gray-300 block truncate",
                ),
                rx.el.span(
                    source, class_name="text-[10px] text-gray-500 block truncate"
                ),
                class_name="min-w-0 flex-1",
            ),
            class_name="flex items-center w-full",
        ),
        href=source,
        target="_blank",
        rel="noopener noreferrer",
        class_name="flex items-center p-2 rounded-lg bg-[#252529] border border-white/5 hover:bg-[#2a2a2e] hover:border-white/10 transition-all duration-200 w-48 shrink-0 cursor-pointer",
    )