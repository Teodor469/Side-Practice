inventory = [] #CHECKED

def add_product():
    name_of_new_product = input("What's the name of the new product? ")
    price_of_new_product = float(input("What's the price of the new product? "))
    quantity_of_new_product = int(input("What's the quantity of the new product? "))
    new_product = {"Name": name_of_new_product, "price": price_of_new_product, "quantity": quantity_of_new_product}
    inventory.append(new_product)
    print("New product added!") #CHECKED

def remove_product():
    product_to_remove = input("Select a product to remove: ")
    items_to_remove = []
    for product in inventory:
        if product['Name'] == product_to_remove:
            items_to_remove.append(product)
    if items_to_remove:
            for item in items_to_remove:
                inventory.remove(item)
                print(f"{product_to_remove} removed from inventory.")
                break
    else:
        print(f"No product with the name {product_to_remove} found in inventory.") #CHECKED

def update_quantity():
    product_to_add_name = input("Update the quantity of any products: ")
    product_to_add_quantity = int(input("Add the updated quantity: "))
    for product in inventory:
        if product["Name"] == product_to_add_name:
            product["quantity"] = product_to_add_quantity
            print(f"Quantity for {product_to_add_name} updated to {product_to_add_quantity}.") #CHECKED
            break

def display_inventory():
    print(inventory)

def sum_values_of_products():
    total_price = 0

    for product in inventory:
        total_price += float(product["price"]) * int(product["quantity"])
    print(f"Total price of all products: {total_price:.2f}") #CHECKED

while True:
    print("\nMenu:")
    print("1. Add product")
    print("2. Remove product")
    print("3. Update quantity")
    print("4. Display inventory")
    print("5. Total price of all products")
    print("6. Exit")
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        add_product()
    elif choice == '2':
        remove_product()
    elif choice == '3':
        update_quantity()
    elif choice == '4':
        display_inventory()
    elif choice == '5':
        sum_values_of_products()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please enter a valid option.")