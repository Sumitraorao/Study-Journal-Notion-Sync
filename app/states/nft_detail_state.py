import reflex as rx
from typing import TypedDict
import random
import asyncio
import logging
from datetime import datetime, timedelta


class Bid(TypedDict):
    id: str
    user: str
    price: float
    time: str
    is_mine: bool


class PricePoint(TypedDict):
    date: str
    price: float


class Property(TypedDict):
    type: str
    value: str
    rarity: str


class NFTDetailState(rx.State):
    nft_id: str = ""
    title: str = "Cosmic Dreams #001"
    creator_name: str = "Joe September"
    creator_handle: str = "@Mr.Rocket68"
    owner_name: str = "CryptoWhale"
    description: str = "A journey through the digital cosmos, exploring the boundaries between reality and imagination. This unique piece features algorithmic generation combined with hand-painted elements."
    current_price: float = 4.1
    currency: str = "ETH"
    time_left: str = "1d 11h 36m 42s"
    likes: int = 245
    is_liked: bool = False
    bid_amount: str = ""
    is_placing_bid: bool = False
    show_bid_modal: bool = False
    bids: list[Bid] = [
        {
            "id": "1",
            "user": "@Collector_One",
            "price": 4.1,
            "time": "2 mins ago",
            "is_mine": False,
        },
        {
            "id": "2",
            "user": "@ArtLover",
            "price": 3.8,
            "time": "15 mins ago",
            "is_mine": False,
        },
        {
            "id": "3",
            "user": "@CryptoKing",
            "price": 3.5,
            "time": "1 hour ago",
            "is_mine": False,
        },
        {
            "id": "4",
            "user": "@EarlyBird",
            "price": 2.0,
            "time": "5 hours ago",
            "is_mine": False,
        },
    ]
    price_history: list[PricePoint] = [
        {"date": "Nov 1", "price": 1.2},
        {"date": "Nov 5", "price": 1.5},
        {"date": "Nov 10", "price": 2.1},
        {"date": "Nov 15", "price": 1.8},
        {"date": "Nov 20", "price": 3.2},
        {"date": "Nov 25", "price": 4.1},
    ]
    properties: list[Property] = [
        {"type": "Background", "value": "Nebula Blue", "rarity": "5%"},
        {"type": "Eyes", "value": "Laser Red", "rarity": "2%"},
        {"type": "Skin", "value": "Chrome", "rarity": "12%"},
        {"type": "Clothing", "value": "Space Suit", "rarity": "8%"},
        {"type": "Accessory", "value": "Cyber Katana", "rarity": "1%"},
        {"type": "Mouth", "value": "Smile", "rarity": "15%"},
    ]
    active_tab: str = "history"

    @rx.event
    def set_active_tab(self, tab: str):
        self.active_tab = tab

    @rx.event
    def set_bid_amount(self, amount: str):
        self.bid_amount = amount

    @rx.event
    def toggle_like(self):
        self.is_liked = not self.is_liked
        if self.is_liked:
            self.likes += 1
        else:
            self.likes -= 1

    @rx.event
    async def place_bid(self):
        try:
            amount = float(self.bid_amount)
            if amount <= self.current_price:
                yield rx.toast(
                    "Bid must be higher than current price!", position="bottom-right"
                )
                return
        except ValueError as e:
            logging.exception(f"Error parsing bid amount: {e}")
            yield rx.toast("Please enter a valid amount", position="bottom-right")
            return
        self.is_placing_bid = True
        yield
        await asyncio.sleep(1.5)
        new_bid: Bid = {
            "id": str(random.randint(1000, 9999)),
            "user": "@You",
            "price": amount,
            "time": "Just now",
            "is_mine": True,
        }
        self.bids.insert(0, new_bid)
        self.current_price = amount
        self.price_history.append({"date": "Nov 26", "price": amount})
        self.is_placing_bid = False
        self.bid_amount = ""
        yield rx.toast("Bid placed successfully!", position="bottom-right")

    @rx.event
    def copy_link(self):
        yield rx.set_clipboard(f"https://nftrade.app/nft/{self.nft_id}")
        yield rx.toast("Link copied to clipboard!", position="bottom-right")

    @rx.event
    def on_load_nft(self):
        pass