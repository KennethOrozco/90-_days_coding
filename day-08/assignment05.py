def order_total(order):
    return order['price'] * order['quantity']

def subtotal(orders):
    return sum(order_total(order) for order in orders)


def final_total(orders, tax_rate=0.08):
    sub = subtotal(orders)
    tax = sub * tax_rate
    return sub + tax

orders = [
    {"name": "Laptop", "price": 1000, "quantity": 2},
    {"name": "Mouse", "price": 25, "quantity": 4},
    {"name": "Monitor", "price": 300, "quantity": 2}
]



print(subtotal(orders))

print(final_total(orders))