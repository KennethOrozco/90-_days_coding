class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def inventory_value(self):
        return self.price * self.quantity

    def sell(self, amount):
        if not isinstance(amount, int):
            raise TypeError("Amount must be an integer")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        if amount > self.quantity:
            raise ValueError("Not enough inventory")
        self.quantity -= amount
        return self.quantity

class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)   

    def total_value(self):
        return(sum(product.inventory_value() for product in self.products))

    def find_product(self, name):
        for product in self.products:
            if name.lower() == product.name.lower():
                return product
        return None
    def sell_product(self, name, amount):
        found = self.find_product(name)
        if found is None:
            raise ValueError("Product not found")
        found.sell(amount)
        return found.quantity

    def remove_product(self, name):
        found = self.find_product(name)
        if found is None:
            raise ValueError("Product not found")
        self.products.remove(found)
        return found

        



    

keyboard = Product("Keyboard", 75, 10)
mouse = Product("Mouse", 40, 5)

inventory = Inventory()

found = inventory.find_product("keyboard")




inventory.add_product(keyboard)
inventory.add_product(mouse)

removed = inventory.remove_product("mouse")
print(removed.name)
print(inventory.find_product("mouse"))