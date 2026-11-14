def create_order(name, price, quantity):
    if price < 0 or quantity < 0 or not name.strip():
        return None
    order = {
        "name": name,
        "price": price,
        "quantity":quantity,
        "total": price * quantity
    }
    return order


def get_order_from_user():
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    order = create_order(name, price, quantity)
    if order:
        print("Order has been recieved!")
        return order
    else:
        print("Invalid order!")
        return None

print(get_order_from_user())

