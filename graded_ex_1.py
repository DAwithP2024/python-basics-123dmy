# Products available in the store by category
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

    for product, price in sorted_products:
        print(f"{product}: ${price:.2f}")

def display_products(products_list):
    for product, price in products_list:
        print(f"{product}: ${price:.2f}")

def display_categories():
    for category in products.keys():
        print(category)

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

    receipt += f"\nTotal cost: ${total_cost:.2f}"
    return receipt

def validate_name(name):
    return bool(name) and all(char.isalpha() or char.isspace() for char in name)

def validate_email(email):
    return "@" in email and "." in email

def main():
    cart = {}
    while True:
        print("Welcome to the store!")
        display_categories()
        category = input("Select a category: ").strip()
        
        if category not in products:
            print("Invalid category. Please try again.")
            continue
        
        display_products(products[category])
        
        product = input("Enter the product name to add to the cart: ").strip()
        quantity = int(input("Enter the quantity: "))
        
        add_to_cart(cart, product, quantity)
        
        print("Current cart:")
        display_cart(cart)
        
        continue_shopping = input("Do you want to continue shopping? (yes/no): ").strip().lower()
        if continue_shopping != "yes":
            break

    name = input("Enter your name: ").strip()
    if not validate_name(name):
        print("Invalid name. Please try again.")
        return

    email = input("Enter your email: ").strip()
    if not validate_email(email):
        print("Invalid email. Please try again.")
        return

    address = input("Enter your address: ").strip()
    
    # Calculate total cost
    total_cost = 0
    for product, quantity in cart.items():
        for category_products in products.values():
            for p, price in category_products:
                if p == product:
                    total_cost += price * quantity
                    break
    
    # Generate and print receipt
    receipt = generate_receipt(name, email, cart, total_cost, address)
    print(receipt)

if __name__ == "__main__":
    main()
