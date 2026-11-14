class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)


keyboard = Product("Keyboard", 75, 10)
mouse = Product("Mouse", 40, 5)

inventory = Inventory()

inventory.add_product(keyboard)
inventory.add_product(mouse)

print(len(inventory.products))
print(inventory.products[0].name)
print(inventory.products[1].name)
    