def category_averages(sales):
    total = {}
    count = {}
    averages = {}
    for sale in sales:
        total[sale['category']] = total.get(sale['category'], 0) + sale['amount']
        count[sale['category']] = count.get(sale['category'], 0) + 1
    for key in total:
        average = total[key] / count[key]
        averages[key] = average
    return averages

def rank_categories(sales):
    averages = category_averages(sales)
    highest = sorted(averages.items(), key=lambda category:category[1],reverse=True)
    names = [name[0] for name in highest]
    return names
    

sales = [
    {"product": "Laptop", "category": "Electronics", "amount": 1200},
    {"product": "Mouse", "category": "Electronics", "amount": 25},
    {"product": "Desk", "category": "Furniture", "amount": 400},
    {"product": "Keyboard", "category": "Electronics", "amount": 75},
    {"product": "Charir", "category": "Furniture", "amount": 200},
    {"product": "Notebook", "category": "Office", "amount": 10},
    {"product": "Pen Set", "category": "Office", "amount": 20}
]

for index, sale in enumerate(rank_categories(sales), start=1):
    print(f"{index}. {sale}")