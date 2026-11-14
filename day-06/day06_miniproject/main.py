import inventory_manager

file_path = r"C:\Users\koroz\90-days-coding\day-06\day06_miniproject\inventory.json"

inventory = inventory_manager.load_inventory(file_path)

options = {
    1: "View Inventory",
    2: "View Total Inventory Value",
    3: "Add Product",
    4: "Update Product Quantity",
    5: "View Low Stock",
    6: "View Category Values",
    7: "Rank Products By Value",
    8: "Find Product",
    9: "Exit"
    }


while True:
    for key, value in options.items():
        print(f"{key}. {value}")
    option = input("Enter the number that corresponds with the option you would like: ")
    if option == "1":
        for product in inventory:
            print(product)
    elif option == "2":
        print(inventory_manager.inventory_value(inventory))
    elif option == "3":
        while True:
            name = input("Choose a product to add: ")
            if name.strip():
                break
            else:
                print("Enter a product!")
        while True:
            category = input("What is it's category?")
            if category.strip():
                break
            else:
                print("Enter a category!")
        while True:
            try:
                price = int(input("What is it's price? "))
                if price >= 0:
                    break
                print("enter a non_negative integer")
            except ValueError:
                print("Type an integer")
        while True:
            try:
                quantity = int(input("What is it's quantity?"))
                if quantity >= 0:
                    break
                print("enter a non_negative integer")
            except ValueError:
                print("Type an integer")
        inventory_manager.add_product(inventory, name, category, price, quantity)
        inventory_manager.save_inventory(inventory, file_path)
        print("Product was added!")
    elif option == "4":
        while True:
            name = input("Choose the product that you would like to update: ")
            if name.strip():
                break
            else:
                print("Type a name!")
        while True:
            try:
                quantity = int(input("What is its update count?"))
                if quantity >= 0:
                    break
                print("enter a non-negative integer!")
            except ValueError:
                print("Enter an integer!")
        update = inventory_manager.update_quantity(inventory, name, quantity)
        if update:
            print("Product was updated!")
            inventory_manager.save_inventory(inventory, file_path)
        else:
            print("Update failed!")
    elif option == "5":
        print(inventory_manager.low_stock(inventory))
    elif option == "6":
        for category, value in inventory_manager.category_values(inventory).items():
            print(f"{category}: {value}")
    elif option == "7":
        for index, product in enumerate(inventory_manager.rank_products(inventory), start=1):
            print(f"{index}. {product['name']}")
    elif option == "8":
        while True:
            name = input("Type product to search: ")
            if name.strip():
                break
            print("Type the name of the product!")
        find = inventory_manager.find_product(inventory, name)
        if find:
            print(find)
        else:
            print("Product not found!")
    elif option == "9":
        break
    else:
        print("Invalid option!")

