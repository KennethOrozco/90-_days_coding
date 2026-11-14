def customer_totals(orders):
    customer = {}
    for order in orders:
        customer[order['customer']] = customer.get(order['customer'], 0) + order['total']
    return customer


def top_customers(orders):
    totals = customer_totals(orders)
    if not totals:
        return []
    highest = max(totals.values())
    top = [customer for customer, total in totals.items() if total == highest]
    return top


orders = [
    {"customer": "Alex", "total": 120},
    {"customer": "Jordan", "total": 75},
    {"customer": "Alex", "total": 50},
    {"customer": "Taylor", "total": 200},
    {"customer": "Jordan", "total": 125},
    {"customer": "Alex", "total": 30}
]

print(top_customers(orders))

