import json
from typing import List, Optional
import products
from cart import dao
from products import Product


class Cart:
    def _init_(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @classmethod
    def load(cls, data: dict) -> "Cart":
        """
        Factory method to create a Cart instance from a dictionary.
        """
        return cls(
            id=data.get("id"),
            username=data.get("username"),
            contents=data.get("contents", []),
            cost=data.get("cost", 0.0),
        )


def get_cart(username: str) -> List[Product]:
    """
    Fetches the cart details for a given user and returns a list of Product objects.
    """
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    try:
        # Parse and load products in one step
        items = [
            products.get_product(product_id)
            for cart_detail in cart_details
            for product_id in json.loads(cart_detail["contents"])
        ]
        return items
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        # Handle errors during parsing or missing data
        print(f"Error loading cart contents: {e}")
        return []


def add_to_cart(username: str, product_id: int) -> None:
    """
    Adds a product to the user's cart.
    """
    try:
        dao.add_to_cart(username, product_id)
    except Exception as e:
        print(f"Error adding product to cart: {e}")


def remove_from_cart(username: str, product_id: int) -> None:
    """
    Removes a product from the user's cart.
    """
    try:
        dao.remove_from_cart(username, product_id)
    except Exception as e:
        print(f"Error removing product from cart: {e}")


def delete_cart(username: str) -> None:
    """
    Deletes the entire cart for a user.
    """
    try:
        dao.delete_cart(username)
    except Exception as e:
        print(f"Error deleting cart: {e}")