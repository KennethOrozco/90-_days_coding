def customer_summary(orders):
    summary = {}
    for order in orders:
        name = order['customer']
        if name not in summary:
            summary[name] = {"orders": 0,"spent": 0}
        summary[name]['orders'] += 1
        summary[name]['spent'] += order['total']
    return summary

def top_spenders(orders):
    highest = 0
    summary = customer_summary(orders)
    for customer in summary:
        if summary[customer]['spent'] > highest:
            highest = summary[customer]['spent']
    return [customer for customer in summary if summary[customer]['spent'] == highest]







orders = [
    {"customer": "Alex", "category": "Electronics", "total": 1200},
    {"customer": "Jordan", "category": "Books", "total": 80},
    {"customer": "Alex", "category": "Books", "total": 50},
    {"customer": "Taylor", "category": "Electronics", "total": 600},
    {"customer": "Jordan", "category": "Electronics", "total": 300},
    {"customer": "Alex", "category": "Electronics", "total": 400},
]

print(top_spenders(orders))