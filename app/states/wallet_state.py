import reflex as rx
from typing import TypedDict
import asyncio
import random
from app.states.nft_state import NFTListing


class Transaction(TypedDict):
    id: str
    type: str
    item_name: str
    price: float
    date: str
    status: str
    hash: str


class WalletState(rx.State):
    is_connected: bool = False
    wallet_address: str = ""
    balance: float = 0.0
    show_modal: bool = False
    is_connecting: bool = False
    username: str = "Unnamed User"
    bio: str = "Digital art collector and creator."
    email: str = ""
    avatar: str = "https://api.dicebear.com/9.x/notionists/svg?seed=user123"
    owned_nfts: list[NFTListing] = [
        {
            "id": "101",
            "title": "Cyber Punk #99",
            "artist": "@FutureVibe",
            "price": 0.8,
            "current_bid": 0.0,
            "image_gradient": "from-purple-600 to-blue-600",
            "category": "Art",
            "ends_in": "Ended",
            "views": 120,
        },
        {
            "id": "102",
            "title": "Glitch Face",
            "artist": "@Lighterman",
            "price": 1.2,
            "current_bid": 0.0,
            "image_gradient": "from-green-400 to-cyan-500",
            "category": "Art",
            "ends_in": "Ended",
            "views": 450,
        },
    ]
    created_nfts: list[NFTListing] = []
    favorited_nfts: list[NFTListing] = []
    transactions: list[Transaction] = [
        {
            "id": "tx1",
            "type": "Purchase",
            "item_name": "Cyber Punk #99",
            "price": 0.8,
            "date": "2023-11-20",
            "status": "Completed",
            "hash": "0x123...abc",
        },
        {
            "id": "tx2",
            "type": "Bid",
            "item_name": "Cosmic Dreams #001",
            "price": 0.5,
            "date": "2023-11-22",
            "status": "Pending",
            "hash": "0x456...def",
        },
    ]
    active_tab: str = "owned"

    @rx.event
    def set_active_tab(self, tab: str):
        self.active_tab = tab

    @rx.event
    def toggle_modal(self):
        self.show_modal = not self.show_modal

    @rx.event
    async def connect_wallet(self, provider: str):
        self.is_connecting = True
        yield
        await asyncio.sleep(1.5)
        self.is_connected = True
        self.wallet_address = (
            f"0x{random.randint(100000, 999999)}...{random.randint(1000, 9999)}"
        )
        self.balance = round(random.uniform(0.5, 15.0), 2)
        self.show_modal = False
        self.is_connecting = False
        yield rx.toast(
            f"Connected to {provider} successfully!", position="bottom-right"
        )

    @rx.event
    def disconnect_wallet(self):
        self.is_connected = False
        self.wallet_address = ""
        self.balance = 0.0
        yield rx.toast("Wallet disconnected", position="bottom-right")

    @rx.event
    def update_settings(self, form_data: dict):
        self.username = form_data.get("username", self.username)
        self.bio = form_data.get("bio", self.bio)
        self.email = form_data.get("email", self.email)
        yield rx.toast("Profile updated successfully!", position="bottom-right")