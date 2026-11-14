class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class ElectricCar(Vehicle):
    def __init__(self, brand, year, battery_size):
        super().__init__(brand, year)
        self.battery_size = battery_size