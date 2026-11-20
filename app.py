from datetime import datetime
from controller import ProductController
from view import show_menu


def request_logger(command):
    print(f"\n[LOG] {datetime.now():%H:%M:%S} {command}")


def main():
    controller = ProductController()
    while True:
        print("\n" + show_menu())
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            request_logger("list_products")
            print(controller.list_products())
        elif choice == "2":
            name = input("Enter product name: ")
            price = input("Enter product price: ")
            request_logger("add_product")
            print(controller.add_product(name, price))
        elif choice == "3":
            product_id = input("Enter product ID: ")
            request_logger("search_product")
            print(controller.search_product(product_id))
        elif choice == "4":
            product_id = input("Enter product ID: ")
            request_logger("delete_product")
            print(controller.delete_product(product_id))
        elif choice == "5":
            request_logger("exit")
            print("Thank you for using Product Catalogue!")
            break
        else:
            request_logger("invalid_command")
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
