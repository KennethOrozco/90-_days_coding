def update_quantity(product, quantity):
    if not isinstance(quantity, int):
        raise TypeError("Quantity must be an integer")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    product["quantity"] = quantity



product = {
    "name": "Keyboard",
    "quantity": 10
}

while True:
    try:
        quantity = int(input("New quantity: "))
        update_quantity(product, quantity)
    except TypeError as error:
        print(error)
    except ValueError as error:
        print(error)
    else:
        print(product)
        break

print(product)