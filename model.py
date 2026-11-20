import json
from pathlib import Path


class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price}


class ProductRepository:
    def __init__(self, filename="products.json"):
        self.filename = Path(__file__).resolve().parent / filename
        if not self.filename.exists():
            self.save_products([])

    def get_all_products(self):
        with self.filename.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return [Product(item["id"], item["name"], item["price"]) for item in data]

    def save_products(self, products):
        with self.filename.open("w", encoding="utf-8") as file:
            json.dump([product.to_dict() for product in products], file, indent=4)

    def add_product(self, name, price):
        products = self.get_all_products()
        new_id = max((product.id for product in products), default=0) + 1
        product = Product(new_id, name, price)
        products.append(product)
        self.save_products(products)
        return product

    def get_product_by_id(self, product_id):
        return next((p for p in self.get_all_products() if p.id == product_id), None)

    def delete_product(self, product_id):
        products = self.get_all_products()
        remaining = [p for p in products if p.id != product_id]
        if len(remaining) == len(products):
            return False
        self.save_products(remaining)
        return True
