# Products available in the store by category
import re


products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order="asc"):
    if sort_order == "asc":
        sorted_products = sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        sorted_products = sorted(products_list, key=lambda x: x[1], reverse=True)
    else:
        raise ValueError("Invalid sort order. Use 'asc' or 'desc'.")

    for index, (product, price) in enumerate(sorted_products, 1):
        print(f"{index}. {product}: ${price:.2f}")

def display_products(products_list):
    for index, (product, price) in enumerate(products_list, 1):
        print(f"{index}. {product}: ${price:.2f}")

def display_categories():
    for index, category in enumerate(products.keys(), 1):
        print(f"{index}. {category}")

def add_to_cart(cart, product, quantity):
    if product in cart:
        cart[product] += quantity
    else:
        cart[product] = quantity

def display_cart(cart):
    total_cost = 0
    print("Cart contents:")
    for product, quantity in cart.items():
        # Find the product's price
        for category_products in products.values():
            for p, price in category_products:
                if p == product:
                    total_price = price * quantity
                    total_cost += total_price
                    print(f"{product} x{quantity}: ${total_price:.2f}")
                    break

    print(f"Total cost: ${total_cost:.2f}")

def generate_receipt(name, email, cart, total_cost, address):
    receipt = (
        f"Receipt\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Address: {address}\n\n"
        f"Items:\n"
    )

    for product, quantity in cart.items():
        # Find the product's price
        for category_products in products.values():
            for p, price in category_products:
                if p == product:
                    total_price = price * quantity
                    receipt += f"{product} x{quantity}: ${total_price:.2f}\n"
                    break

    receipt += f"\nTotal cost: ${total_cost:.2f}\n"
    receipt += "Your items will be delivered in 3 days. Payment will be accepted after successful delivery."
    return receipt

def validate_name(name):
    parts = name.split()
    if len(parts) != 2:
        return False
    first_name, last_name = parts
    return all(part.isalpha() for part in parts)

def validate_email(email):
    # Regex pattern to validate email address
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def main():
    while True:
        # User input and validation
        name = input("Enter your name (First Last): ").strip()
        while not validate_name(name):
            print("Invalid name. Please enter a valid name (First Last).")
            name = input("Enter your name (First Last): ").strip()

        email = input("Enter your email: ").strip()
        while not validate_email(email):
            print("Invalid email. Please enter a valid email address.")
            email = input("Enter your email: ").strip()

        # Display categories
        display_categories()
        category_choice = int(input("Select a category by number: "))
        category_list = list(products.keys())

        if 1 <= category_choice <= len(category_list):
            category = category_list[category_choice - 1]
        else:
            print("Invalid category choice. Exiting.")
            return

        cart = {}
        while True:
            # Display products in the chosen category
            print(f"\nProducts in {category}:")
            display_products(products[category])

            # Options
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort the products by price")
            print("3. Go back to the category selection")
            print("4. Finish shopping")

            option = int(input("Choose an option: "))

            if option == 1:
                product_choice = int(input("Enter the product number to buy: "))
                if 1 <= product_choice <= len(products[category]):
                    product, price = products[category][product_choice - 1]
                    quantity = int(input(f"Enter the quantity for {product}: "))
                    add_to_cart(cart, product, quantity)
                else:
                    print("Invalid product choice. Please try again.")
            elif option == 2:
                sort_order = input("Sort by price ascending (1) or descending (2)? ").strip()
                if sort_order in ["1", "2"]:
                    sort_order = "asc" if sort_order == "1" else "desc"
                    print(f"\nProducts in {category} sorted by price {sort_order}:")
                    display_sorted_products(products[category], sort_order)
                else:
                    print("Invalid choice. Returning to options.")
            elif option == 3:
                break
            elif option == 4:
                if cart:
                    print("\nYour cart:")
                    display_cart(cart)
                    total_cost = sum(products[category][product][1] * quantity for product, quantity in cart.items())
                    address = input("Enter your delivery address: ").strip()
                    receipt = generate_receipt(name, email, cart, total_cost, address)
                    print("\n" + receipt)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day!")
                return
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
