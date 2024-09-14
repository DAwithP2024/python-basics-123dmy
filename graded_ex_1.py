import re

# Validate Name (Only allows names with spaces and alphabets)
def validate_name(name):
    # Match names that contain only letters and spaces, and at least one space between words
    return bool(re.match(r'^[A-Za-z]+( [A-Za-z]+)+$', name))

# Validate Email (Basic email validation)
def validate_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+$', email))

# Display Categories
def display_categories():
    categories = ["Electronics", "Books", "Clothing", "Groceries"]
    print("Categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    try:
        choice = int(input("Choose a category (number): ")) - 1
        if 0 <= choice < len(categories):
            return choice
        else:
            print("Invalid choice.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def display_sorted_products(products_list, order):
    if order == "asc":
        return sorted(products_list, key=lambda x: x[1])
    elif order == "desc":
        return sorted(products_list, key=lambda x: x[1], reverse=True)
    return products_list

# Add product to cart
def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))
    print(f"Added {quantity} x {product[0]} to the cart.")

# Display cart contents
def display_cart(cart):
    total_cost = 0
    for item in cart:
        name, price, quantity = item
        cost = price * quantity
        total_cost += cost
        print(f"{name} - ${price} x {quantity} = ${cost}")
    print(f"Total cost: ${total_cost}")

# Generate receipt (For future use)
def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for item in cart:
        name, price, quantity = item
        print(f"{quantity} x {name} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")

# Example product list for categories (This can be expanded)
products = [
    [("Laptop", 1000), ("Smartphone", 600), ("USB Drive", 15)],  # Electronics
    [("Book1", 20), ("Book2", 30)],  # Books
    [("T-shirt", 25), ("Jeans", 40)],  # Clothing
    [("Apple", 1), ("Banana", 0.5)]   # Groceries
]

# Main program flow (for integration with testing)
def main():
    cart = []
    
    # Name validation
    name = input("Enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid name.")
        name = input("Enter your name: ")

    # Email validation
    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email.")
        email = input("Enter your email: ")

    # Category selection
    category_index = display_categories()
    if category_index is None:
        print("No valid category selected.")
        return
    
    # Display products
    selected_products = products[category_index]
    print("Products in this category:")
    for i, product in enumerate(selected_products, 1):
        print(f"{i}. {product[0]} - ${product[1]}")

    # Sort products by user choice
    sort_order = input("Sort products by price (asc/desc): ").strip().lower()
    sorted_products = display_sorted_products(selected_products, sort_order)
    print("Sorted Products:")
    for i, product in enumerate(sorted_products, 1):
        print(f"{i}. {product[0]} - ${product[1]}")

    # Product selection
    product_choice = input("Choose a product to add to cart (number): ")
    if not product_choice.isdigit() or not (1 <= int(product_choice) <= len(sorted_products)):
        print("Invalid product choice.")
        return
    product_index = int(product_choice) - 1
    selected_product = sorted_products[product_index]

    # Quantity selection
    quantity = input(f"How many {selected_product[0]}s would you like to buy? ")
    if not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid quantity.")
        return

    # Add to cart
    add_to_cart(cart, selected_product, int(quantity))

    # Display cart
    display_cart(cart)


if __name__ == "__main__":
    main()
