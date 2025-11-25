import reflex as rx
from typing import TypedDict


class Creator(TypedDict):
    id: str
    name: str
    handle: str
    avatar_seed: str
    cover_gradient: str
    collection_value: str
    followers: str
    is_followed: bool
    artwork_gradients: list[str]


class NFTListing(TypedDict):
    id: str
    title: str
    artist: str
    price: float
    current_bid: float
    image_gradient: str
    category: str
    ends_in: str
    views: int


class NftState(rx.State):
    active_category: str = "All"
    search_query: str = ""
    sort_option: str = "Recently Added"
    is_loading_marketplace: bool = True
    categories: list[str] = [
        "All",
        "Art",
        "Photography",
        "Games",
        "Music",
        "Collectibles",
    ]
    sort_options: list[str] = [
        "Recently Added",
        "Price: Low to High",
        "Price: High to Low",
        "Ending Soon",
    ]
    listings: list[NFTListing] = [
        {
            "id": "1",
            "title": "Cosmic Dreams #001",
            "artist": "@Mr.Rocket68",
            "price": 1.2,
            "current_bid": 0.8,
            "image_gradient": "from-purple-500 to-indigo-500",
            "category": "Art",
            "ends_in": "12h 43m",
            "views": 1204,
        },
        {
            "id": "2",
            "title": "Neon Genesis",
            "artist": "@Lighterman",
            "price": 0.5,
            "current_bid": 0.25,
            "image_gradient": "from-cyan-400 to-blue-600",
            "category": "Photography",
            "ends_in": "2d 1h",
            "views": 856,
        },
        {
            "id": "3",
            "title": "Pixel Warrior",
            "artist": "@GameMaster",
            "price": 2.5,
            "current_bid": 2.1,
            "image_gradient": "from-emerald-400 to-teal-600",
            "category": "Games",
            "ends_in": "4h 20m",
            "views": 3402,
        },
        {
            "id": "4",
            "title": "Abstract Thoughts",
            "artist": "@WhiteArt70",
            "price": 5.0,
            "current_bid": 4.8,
            "image_gradient": "from-rose-400 to-orange-500",
            "category": "Art",
            "ends_in": "1d 10h",
            "views": 5600,
        },
        {
            "id": "5",
            "title": "Cyber Punk City",
            "artist": "@FutureVibe",
            "price": 0.85,
            "current_bid": 0.4,
            "image_gradient": "from-fuchsia-500 to-pink-600",
            "category": "Art",
            "ends_in": "5h 30m",
            "views": 920,
        },
        {
            "id": "6",
            "title": "Sound Wave X",
            "artist": "@AudioPhile",
            "price": 1.1,
            "current_bid": 0.9,
            "image_gradient": "from-yellow-400 to-orange-500",
            "category": "Music",
            "ends_in": "8h 15m",
            "views": 150,
        },
        {
            "id": "7",
            "title": "Golden Ticket",
            "artist": "@CollectorKing",
            "price": 10.0,
            "current_bid": 9.5,
            "image_gradient": "from-amber-300 to-yellow-600",
            "category": "Collectibles",
            "ends_in": "30m 05s",
            "views": 8900,
        },
        {
            "id": "8",
            "title": "Virtual Reality",
            "artist": "@VR_Artist",
            "price": 3.2,
            "current_bid": 3.0,
            "image_gradient": "from-sky-400 to-indigo-500",
            "category": "Games",
            "ends_in": "1d 5h",
            "views": 2100,
        },
    ]
    top_creators: list[Creator] = [
        {
            "id": "1",
            "name": "Joe September",
            "handle": "@Mr.Rocket68",
            "avatar_seed": "joe",
            "cover_gradient": "from-cyan-400/20 to-blue-600/20",
            "collection_value": "$1,000,000",
            "followers": "12,990",
            "is_followed": False,
            "artwork_gradients": [
                "from-pink-500 to-rose-500",
                "from-purple-500 to-indigo-500",
                "from-cyan-500 to-blue-500",
            ],
        },
        {
            "id": "2",
            "name": "Liam Lighter",
            "handle": "@Lighterman",
            "avatar_seed": "liam",
            "cover_gradient": "from-red-500/20 to-orange-600/20",
            "collection_value": "$983,000",
            "followers": "14,008",
            "is_followed": True,
            "artwork_gradients": [
                "from-emerald-500 to-teal-500",
                "from-orange-500 to-amber-500",
                "from-gray-700 to-gray-900",
            ],
        },
        {
            "id": "3",
            "name": "Sally Salt",
            "handle": "@WhiteArt70",
            "avatar_seed": "sally",
            "cover_gradient": "from-purple-500/20 to-pink-600/20",
            "collection_value": "$2,083,005",
            "followers": "48,205",
            "is_followed": False,
            "artwork_gradients": [
                "from-white to-gray-300",
                "from-blue-200 to-cyan-200",
                "from-indigo-300 to-purple-300",
            ],
        },
        {
            "id": "4",
            "name": "Beata Dubas",
            "handle": "@Give_me_stars",
            "avatar_seed": "beata",
            "cover_gradient": "from-amber-400/20 to-yellow-600/20",
            "collection_value": "$509,000",
            "followers": "9,773",
            "is_followed": False,
            "artwork_gradients": [
                "from-rose-300 to-pink-400",
                "from-fuchsia-400 to-purple-500",
                "from-violet-500 to-indigo-600",
            ],
        },
    ]
    newsletter_email: str = ""
    subscribed: bool = False

    @rx.event
    def toggle_follow(self, creator_id: str):
        for creator in self.top_creators:
            if creator["id"] == creator_id:
                creator["is_followed"] = not creator["is_followed"]
                break

    @rx.event
    def set_newsletter_email(self, email: str):
        self.newsletter_email = email

    @rx.event
    def subscribe_newsletter(self):
        if self.newsletter_email:
            self.subscribed = True
            return rx.toast("Subscribed successfully!", position="bottom-center")

    @rx.event
    def set_active_category(self, category: str):
        self.active_category = category
        self.simulate_loading()

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def set_sort_option(self, option: str):
        self.sort_option = option

    @rx.event
    async def simulate_loading(self):
        self.is_loading_marketplace = True
        yield
        import asyncio

        await asyncio.sleep(0.8)
        self.is_loading_marketplace = False

    @rx.var
    def filtered_listings(self) -> list[NFTListing]:
        filtered = self.listings
        if self.active_category != "All":
            filtered = [
                item for item in filtered if item["category"] == self.active_category
            ]
        if self.search_query:
            query = self.search_query.lower()
            filtered = [
                item
                for item in filtered
                if query in item["title"].lower() or query in item["artist"].lower()
            ]
        if self.sort_option == "Price: Low to High":
            filtered = sorted(filtered, key=lambda x: x["price"])
        elif self.sort_option == "Price: High to Low":
            filtered = sorted(filtered, key=lambda x: x["price"], reverse=True)
        elif self.sort_option == "Ending Soon":
            filtered = sorted(filtered, key=lambda x: x["ends_in"])
        return filtered