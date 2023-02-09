from typing import List


class ShoppingCart:
    def __init__(self, max_size: int = 5) -> None:
        self.items: List[str] = []
        self.max_size = max_size

    def add(self, item: str) -> None:
        if self.size() == self.max_size:
            raise OverflowError("cannot add more items to the list")
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map) -> int:
        return sum(price_map.get(item) for item in self.items)
