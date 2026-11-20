def show_products(products):
    if not products:
        return "No products available."
    output = f"{'ID':<5}{'Name':<20}{'Price':>10}\n" + "-" * 35 + "\n"
    for product in products:
        output += f"{product.id:<5}{product.name:<20}{product.price:>10.2f}\n"
    return output


def show_product(product):
    if product is None:
        return "Product not found."
    return f"ID: {product.id}\nName: {product.name}\nPrice: {product.price:.2f}"


def show_message(message):
    return message


def show_menu():
    return """========== PRODUCT CATALOGUE ==========

1. List Products
2. Add Product
3. Search Product
4. Delete Product
5. Exit

======================================="""
