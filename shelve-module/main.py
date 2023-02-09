import shelve

data = {"a": 1, "b": 2, "c": 3}

with shelve.open("TestDB") as db:
    # db.update(data)
    print(dict(db))


class Fruit:
    def __init__(self, name: str, calories: int) -> None:
        self.name = name
        self.calories = calories

    def __str__(self) -> str:
        return f"{self.name}: {self.calories}"


fruit_data = {
    "apple": Fruit("Apple", 10),
    "banana": Fruit("Banana", 15),
    "orange": Fruit("Orange", 20),
}

with shelve.open("FruitsDB") as db:
    # db.update(fruit_data)
    apple: Fruit = db.get("apple")

print(apple)
