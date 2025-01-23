from products import dao
from typing import List, Dict


class Product:
    def _init_(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def load(cls, data: Dict) -> "Product":
        """
        Factory method to create a Product instance from a dictionary.
        """
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            description=data.get("description"),
            cost=data.get("cost"),
            qty=data.get("qty", 0),
        )


def list_products() -> List[Product]:
    """
    Fetches a list of products and returns them as a list of Product objects.
    """
    try:
        return [Product.load(product) for product in dao.list_products()]
    except Exception as e:
        print(f"Error listing products: {e}")
        return []


def get_product(product_id: int) -> Product:
    """
    Fetches a single product by its ID and returns it as a Product object.
    """
    try:
        product_data = dao.get_product(product_id)
        if product_data:
            return Product.load(product_data)
        raise ValueError(f"Product with ID {product_id} not found.")
    except Exception as e:
        print(f"Error fetching product with ID {product_id}: {e}")
        raise


def add_product(product: Dict):
    """
    Adds a new product using a dictionary of product details.
    """
    try:
        dao.add_product(product)
    except Exception as e:
        print(f"Error adding product: {e}")


def update_qty(product_id: int, qty: int):
    """
    Updates the quantity of a product.
    """
    if qty < 0:
        raise ValueError("Quantity cannot be negative")
    try:
        dao.update_qty(product_id, qty)
    except Exception as e:
        print(f"Error updating quantity for product ID {product_id}: {e}")