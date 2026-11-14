import json

def load_orders(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        print("Invalid JSON data!")
        return []

def save_orders(orders, file_path):
    with open(file_path, "w") as file:
        json.dump(orders, file)

def create_order(customer, product, price, quantity):
    if not customer.strip():
        raise ValueError("Customer cannot be empty")

    if not product.strip():
        raise ValueError("Product cannot be empty")

    if not isinstance(price, (int, float)):
        raise TypeError("Price must be numeric")

    if price < 0:
        raise ValueError("Price cannot be negative")

    if not isinstance(quantity, int):
        raise TypeError("Quantity must be an integer")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    return {
        "customer": customer,
        "product": product,
        "price": price,
        "quantity": quantity,
        "status": "pending"
    }

def order_total(order):
    return order['price'] * order['quantity']

def total_revenue(orders):
    return sum(order_total(order) for order in orders if order['status'] == "completed")

def find_orders(orders, status=None, customer=None):
    filtered = []
    for order in orders:
        match = True
        if status is not None and status.lower() != order['status'].lower():
            match = False

        if customer is not None and customer.lower() != order['customer'].lower():
            match = False

        if match:
            filtered.append(order)
    
    return filtered

def complete_order(orders, index):
    if index < 0 or index >= len(orders):
        raise IndexError("Order does not exist")

    orders[index]['status'] = "completed"
    return True

def validate_orders(orders):
    if not isinstance(orders, list):
        raise TypeError("Orders must be a list")
    
    keys = ["customer", "product", "price", "quantity", "status"]
    
    for order in orders:

        if not isinstance(order, dict):
            raise TypeError("Each order must be a dictionary")

        if not all(key in order for key in keys):
            raise ValueError("Order is missing required data")

        if not isinstance(order['price'], (int, float)):
            raise TypeError("Price must be numeric")

        if not isinstance(order['quantity'], int):
            raise TypeError("Quantity must be an integer")

    return orders
    