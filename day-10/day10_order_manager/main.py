import order_manager

file_path = r"C:\Users\koroz\90-days-coding\day-10\day10_order_manager\orders.json"

orders = order_manager.load_orders(file_path)

try:
    order_manager.validate_orders(orders)
except ValueError as error:
    print(error)
    orders = []
except TypeError as error:
    print(error)
    orders = []

while True:
    options = {
        1: "View Orders",
        2: "Add Order",
        3: "Complete Order",
        4: "Find Orders",
        5: "View Total Revenue",
        6: "Exit"
    }
    for key, value in options.items():
        print(f"{key}. {value}")
    option = input("Choose an option: ")
    if option == "1":
        print(orders)
    elif option == "2":
        try:
            customer = input("Customer: ")
            product = input("Product: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            created = order_manager.create_order(customer, product, price, quantity)
        except ValueError as error:
            print(error)
        except TypeError as error:
            print(error)
        else:
            orders.append(created)
            order_manager.save_orders(orders, file_path)
            print("Order was created!")
    elif option == "3":
        for index, order in enumerate(orders, start=1):
            print(f"{index}. {order['customer']} - {order['product']}")
        while True:
            try:
                index = int(input("Index: "))
                order_manager.complete_order(orders, index - 1)
            except ValueError:
                print("Type an integer!")
            except IndexError as error:
                print(error)
            else:
                    print("Order has been marked completed!")
                    order_manager.save_orders(orders, file_path)
                    break
    elif option == "4":
        status = input("Status (blank for any): ")
        if not status.strip():
            status = None
        customer = input("Customer (blank for any): ")
        if not customer.strip():
            customer = None
        print(order_manager.find_orders(orders, status, customer))
    elif option == "5":
        print(order_manager.total_revenue(orders))
    elif option == "6":
        break
    else:
        print("Invalid opton!")
        


