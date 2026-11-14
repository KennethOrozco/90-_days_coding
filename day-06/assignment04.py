# def process_order(product, price, quantity=1,**details):
#     total = price * quantity
#     dictionary = {
#         "product":product,
#         "price": price,
#         "quantity": quantity,
#         "total": total
#         }
#     dictionary.update(details)
#     return dictionary

# print(process_order("Laptop", 1200, customer="Alex", priority=True))
def cart_total(cart):
    sum_= 0
    for product in cart:
        sum_ += product['price']*product["quantity"]
    return sum_



def order_summary(cart, tax_rate=0.08):
    subtotal= cart_total(cart)
    tax = subtotal * tax_rate
    dictionary= {
        "subtotal": subtotal,
        "tax": tax,
        "total": subtotal + tax
        }
    return dictionary



cart = [
    {"product": "Laptop", "price": 1200, "quantity":1},
    {"product": "Mouse", "price": 25, "quantity": 2},
    {"prodct": "Keyboard", "price": 75, "quantity": 1}
]

print(order_summary(cart))