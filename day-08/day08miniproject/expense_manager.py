import json

def load_expenses(file_path):
    try:
        with open(file_path, "r") as file:
            content = json.load(file)
            return content
    except FileNotFoundError:
        print("File not found!")
        return []

def save_expenses(expenses, file_path):
    with open(file_path, "w") as file:
        json.dump(expenses, file)

def create_expense(description, category, amount):
    if not description.strip() or not category.strip() or amount < 0:
        return None
    create = {
        "description": description,
        "category": category,
        "amount": amount
    }
    return create

def add_expense(expenses, expense):
    expenses.append(expense)

def total_spending(expenses):
    return sum(expense['amount'] for expense in expenses)

def category_summary(expenses):
    summary = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category not in summary:
            summary[category] = {"expenses":0, "spent": 0}

        summary[category]['expenses'] += 1
        summary[category]['spent'] += amount
    return summary

def highest_expense(expenses):
    if not expenses:
        return None
    highest = max(expenses, key=lambda expense:expense['amount'])
    return highest


def filter_by_category(expenses, category):
    filtered = []
    for expense in expenses:
        if category.lower() == expense['category'].lower():
            filtered.append(expense)
    return filtered

