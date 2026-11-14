import json

def load_inventory(file_path):
    try:
        with open(file_path, "r") as file:
            content = json.load(file)
            return content
    except FileNotFoundError:
        print("File not found!")
        return []

def save_inventory(inventory, file_path):
    with open(file_path, "w") as file:
        json.dump(inventory, file)

def inventory_value(inventory):
    total = 0
    for product in inventory:
        total += product['price'] * product['quantity']
    return total

def add_product(inventory, name, category, price, quantity):
    product = {
        "name":name,
        "category": category,
        "price": price,
        "quantity": quantity
    }
    inventory.append(product)

def update_quantity(inventory, name, quantity):
    for product in inventory:
        if product['name'] == name:
            product['quantity'] = quantity
            return True
    return False

def low_stock(inventory, threshold=5):
    return [product for product in inventory if product['quantity'] <= threshold]

def category_values(inventory):
    totals = {}
    for product in inventory:
        total = product['price'] * product["quantity"]
        totals[product['category']] = totals.get(product['category'], 0) + total
    return totals

def rank_products(inventory):
    return sorted(inventory, key=lambda product: product['price'] * product['quantity'], reverse=True)

def find_product(inventory, name):
    for product in inventory:
        if product['name'].lower() == name.lower():
            return product
    return None
