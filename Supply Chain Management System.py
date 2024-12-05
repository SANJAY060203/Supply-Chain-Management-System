# Supply Chain Management System

# Sample Data: Inventory, Suppliers, and Orders
inventory = {
    "Product_A": {"quantity": 100, "price": 50},
    "Product_B": {"quantity": 200, "price": 30},
    "Product_C": {"quantity": 150, "price": 20}
}

suppliers = {
    "Supplier_1": {"products": ["Product_A", "Product_B"], "contact": "supplier1@example.com"},
    "Supplier_2": {"products": ["Product_C"], "contact": "supplier2@example.com"}
}

orders = []  # List to store orders


# Function to display inventory
def view_inventory():
    print("\nCurrent Inventory:")
    for product, details in inventory.items():
        print(f"{product}: Quantity = {details['quantity']}, Price = {details['price']}/unit")
    print()


# Function to place an order
def place_order():
    print("\nAvailable Products:")
    for product in inventory.keys():
        print(f"- {product}")
    
    product_name = input("Enter the product name to order: ")
    if product_name not in inventory:
        print("Error: Product not found in inventory.")
        return

    quantity = int(input(f"Enter the quantity of {product_name} to order: "))
    if quantity > inventory[product_name]["quantity"]:
        print("Error: Insufficient stock.")
        return

    # Process order
    inventory[product_name]["quantity"] -= quantity
    total_cost = quantity * inventory[product_name]["price"]
    orders.append({"product": product_name, "quantity": quantity, "total_cost": total_cost})
    print(f"Order placed successfully! Total cost: {total_cost}\n")


# Function to restock inventory
def restock_inventory():
    product_name = input("Enter the product name to restock: ")
    if product_name not in inventory:
        print("Error: Product not found in inventory.")
        return

    quantity = int(input(f"Enter the quantity of {product_name} to add: "))
    inventory[product_name]["quantity"] += quantity
    print(f"{quantity} units of {product_name} added to inventory.\n")


# Function to view suppliers
def view_suppliers():
    print("\nSuppliers:")
    for supplier, details in suppliers.items():
        print(f"{supplier}: Products = {', '.join(details['products'])}, Contact = {details['contact']}")
    print()


# Function to view order history
def view_orders():
    print("\nOrder History:")
    if not orders:
        print("No orders placed yet.")
    else:
        for i, order in enumerate(orders, 1):
            print(f"Order {i}: Product = {order['product']}, Quantity = {order['quantity']}, Total Cost = {order['total_cost']}")
    print()


# Main menu
def main():
    while True:
        print("Supply Chain Management System")
        print("1. View Inventory")
        print("2. Place Order")
        print("3. Restock Inventory")
        print("4. View Suppliers")
        print("5. View Order History")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            view_inventory()
        elif choice == "2":
            place_order()
        elif choice == "3":
            restock_inventory()
        elif choice == "4":
            view_suppliers()
        elif choice == "5":
            view_orders()
        elif choice == "6":
            print("Exiting Supply Chain Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the system
if __name__ == "__main__":
    main()
