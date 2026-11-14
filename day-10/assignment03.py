def create_product(name, price, quantity):
    if not name.strip():
        raise ValueError("Product name cannot be empty")

    if price < 0:
        raise ValueError("Price cannot be negative")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    return {
        "name": name,
        "price": price,
        "quantity": quantity
    }

try:
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    product = create_product(name, price, quantity)
except ValueError as error:
    print(error)
else:
    print(product)
