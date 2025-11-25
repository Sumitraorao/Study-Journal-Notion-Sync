import reflex as rx
import asyncio
from typing import TypedDict


class Property(TypedDict):
    type: str
    value: str


class CreateNftState(rx.State):
    uploaded_file_name: str = ""
    upload_progress: int = 0
    is_uploading: bool = False
    is_minting: bool = False
    name: str = ""
    description: str = ""
    price: str = ""
    category: str = "Art"
    properties: list[Property] = []
    new_prop_type: str = ""
    new_prop_value: str = ""
    show_success_modal: bool = False

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        if not files:
            return
        self.is_uploading = True
        self.upload_progress = 0
        yield
        for i in range(1, 11):
            await asyncio.sleep(0.1)
            self.upload_progress = i * 10
            yield
        file = files[0]
        upload_data = await file.read()
        outfile = rx.get_upload_dir() / file.name
        with outfile.open("wb") as file_object:
            file_object.write(upload_data)
        self.uploaded_file_name = file.name
        self.is_uploading = False
        yield rx.toast("File uploaded successfully!", position="bottom-right")

    @rx.event
    def set_name(self, val: str):
        self.name = val

    @rx.event
    def set_description(self, val: str):
        self.description = val

    @rx.event
    def set_price(self, val: str):
        self.price = val

    @rx.event
    def set_category(self, val: str):
        self.category = val

    @rx.event
    def set_new_prop_type(self, val: str):
        self.new_prop_type = val

    @rx.event
    def set_new_prop_value(self, val: str):
        self.new_prop_value = val

    @rx.event
    def add_property(self):
        if self.new_prop_type and self.new_prop_value:
            self.properties.append(
                {"type": self.new_prop_type, "value": self.new_prop_value}
            )
            self.new_prop_type = ""
            self.new_prop_value = ""

    @rx.event
    def remove_property(self, index: int):
        self.properties.pop(index)

    @rx.event
    async def mint_nft(self):
        if not self.name or not self.price or (not self.uploaded_file_name):
            yield rx.toast(
                "Please fill in all required fields and upload artwork.",
                position="bottom-right",
            )
            return
        self.is_minting = True
        yield
        await asyncio.sleep(2)
        self.is_minting = False
        self.show_success_modal = True
        self.name = ""
        self.description = ""
        self.price = ""
        self.uploaded_file_name = ""
        self.properties = []

    @rx.event
    def close_success_modal(self):
        self.show_success_modal = False