from unittest.mock import Mock

# pip install pytest
import pytest
from item_database import ItemDatabase
from shopping_cart import ShoppingCart

# PYTEST FIXTURES: avoid duplicate code by putting setup/initialisation in one function
# you can have multiple fixtures passed into one test function


# UNITTEST.MOCK - mocking dependencies in test e.g. a database or an API or an RNG
# to avoid inconsistencies during testing e.g. being affected by database changes/updates
@pytest.fixture
def cart():
    # IMAGINE MASSIVE SETUP CODE HERE
    return ShoppingCart()


# note the naming convention, function and file names start with 'test_'
def test_can_add_item_to_cart(cart):
    cart.add("apple")
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_when_add_more_than_max_items_should_fail(cart):
    for _ in range(5):
        cart.add("apple")

    # check if code enforces the max_size constraint
    # fails if the below exception is NOT THROWN
    with pytest.raises(OverflowError):
        cart.add("apple")


def test_can_get_total_price(cart):
    cart.add("apple")
    cart.add("orange")
    cart.add("orange")
    cart.add("yoghurt")
    cart.add("juice")
    # price_map = {"apple": 10, "orange": 5}

    item_database = ItemDatabase()
    # since the database is incomplete, we can mock it in the test as shown below
    # item_database.get = Mock(return_value=1.0) -> restricts all returns to one value

    def mock_get_item(item: str) -> float:
        return 1.0 if item == "apple" else 2.0 if item == "orange" else 5.0

    item_database.get = Mock(side_effect=mock_get_item)

    assert cart.get_total_price(price_map=item_database) == 15
