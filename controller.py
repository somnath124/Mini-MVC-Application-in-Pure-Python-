from model import ProductRepository
from view import show_products, show_product, show_message


class ProductController:
    def __init__(self):
        self.repository = ProductRepository()

    def list_products(self):
        return show_products(self.repository.get_all_products())

    def add_product(self, name, price):
        try:
            name = name.strip()
            price = float(price)
            if not name:
                return show_message("Error: Product name cannot be empty.")
            if not 0 <= price < float("inf"):
                return show_message("Error: Price must be a finite non-negative number.")
            product = self.repository.add_product(name, price)
            return show_message(f"Product '{product.name}' added successfully!")
        except ValueError:
            return show_message("Error: Invalid price.")

    def search_product(self, product_id):
        try:
            return show_product(self.repository.get_product_by_id(int(product_id)))
        except ValueError:
            return show_message("Error: Invalid product ID.")

    def delete_product(self, product_id):
        try:
            deleted = self.repository.delete_product(int(product_id))
            return show_message("Product deleted successfully!" if deleted else "Product not found.")
        except ValueError:
            return show_message("Error: Invalid product ID.")
