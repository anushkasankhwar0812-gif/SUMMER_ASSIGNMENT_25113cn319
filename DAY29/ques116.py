#write a program to create a inventory management system.
inventory = {}


def add_item():
    item_id = input("Enter item ID: ")
    if item_id in inventory:
        print("Item ID already exists. Use update instead.")
        return

    name = input("Enter item name: ")
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
    except ValueError:
        print("Invalid input. Quantity must be a whole number and price numeric.")
        return

    inventory[item_id] = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    print(f"Item '{name}' added successfully.")


def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    print(f"\n{'ID':<10}{'Name':<20}{'Quantity':<12}{'Price':<10}{'Total Value':<12}")
    print("-" * 64)
    for item_id, details in inventory.items():
        total_value = details["quantity"] * details["price"]
        print(f"{item_id:<10}{details['name']:<20}{details['quantity']:<12}"
              f"{details['price']:<10.2f}{total_value:<12.2f}")


def update_item():
    item_id = input("Enter item ID to update: ")
    if item_id not in inventory:
        print("Item not found.")
        return

    print("Leave field blank to keep current value.")
    name = input(f"Enter new name [{inventory[item_id]['name']}]: ")
    quantity = input(f"Enter new quantity [{inventory[item_id]['quantity']}]: ")
    price = input(f"Enter new price [{inventory[item_id]['price']}]: ")

    if name:
        inventory[item_id]["name"] = name
    if quantity:
        try:
            inventory[item_id]["quantity"] = int(quantity)
        except ValueError:
            print("Invalid quantity. Keeping previous value.")
    if price:
        try:
            inventory[item_id]["price"] = float(price)
        except ValueError:
            print("Invalid price. Keeping previous value.")

    print("Item updated successfully.")


def delete_item():
    item_id = input("Enter item ID to delete: ")
    if item_id in inventory:
        removed = inventory.pop(item_id)
        print(f"Item '{removed['name']}' deleted successfully.")
    else:
        print("Item not found.")


def search_item():
    item_id = input("Enter item ID to search: ")
    if item_id in inventory:
        details = inventory[item_id]
        total_value = details["quantity"] * details["price"]
        print(f"\nID: {item_id}")
        print(f"Name: {details['name']}")
        print(f"Quantity: {details['quantity']}")
        print(f"Price: {details['price']:.2f}")
        print(f"Total Value: {total_value:.2f}")
    else:
        print("Item not found.")


def restock_item():
    item_id = input("Enter item ID to restock: ")
    if item_id not in inventory:
        print("Item not found.")
        return
    try:
        qty = int(input("Enter quantity to add: "))
        inventory[item_id]["quantity"] += qty
        print(f"Stock updated. New quantity: {inventory[item_id]['quantity']}")
    except ValueError:
        print("Invalid quantity.")


def sell_item():
    item_id = input("Enter item ID to sell: ")
    if item_id not in inventory:
        print("Item not found.")
        return
    try:
        qty = int(input("Enter quantity to sell: "))
        if qty > inventory[item_id]["quantity"]:
            print("Insufficient stock.")
        else:
            inventory[item_id]["quantity"] -= qty
            print(f"Sale recorded. Remaining quantity: {inventory[item_id]['quantity']}")
    except ValueError:
        print("Invalid quantity.")


def low_stock_report():
    try:
        threshold = int(input("Enter low stock threshold: "))
    except ValueError:
        print("Invalid threshold.")
        return

    low_items = {k: v for k, v in inventory.items() if v["quantity"] <= threshold}
    if not low_items:
        print("No items below threshold.")
        return

    print(f"\nItems with quantity <= {threshold}:")
    for item_id, details in low_items.items():
        print(f"ID: {item_id}, Name: {details['name']}, Quantity: {details['quantity']}")


def total_inventory_value():
    total = sum(details["quantity"] * details["price"] for details in inventory.values())
    print(f"Total inventory value: {total:.2f}")


def show_menu():
    print("\n----- INVENTORY MANAGEMENT SYSTEM -----")
    print("1.  Add Item")
    print("2.  Display Inventory")
    print("3.  Update Item")
    print("4.  Delete Item")
    print("5.  Search Item")
    print("6.  Restock Item")
    print("7.  Sell Item")
    print("8.  Low Stock Report")
    print("9.  Total Inventory Value")
    print("10. Exit")
    print("----------------------------------------")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            display_inventory()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            search_item()
        elif choice == '6':
            restock_item()
        elif choice == '7':
            sell_item()
        elif choice == '8':
            low_stock_report()
        elif choice == '9':
            total_inventory_value()
        elif choice == '10':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 10.")


if __name__ == "__main__":
    main()