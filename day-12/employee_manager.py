class Employee:
    def __init__(self,name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = new_salary

    def calculate_monthly_pay(self):
        return self.salary / 12

class Developer(Employee):

    def calculate_monthly_pay(self):
        return super().calculate_monthly_pay()

    def __str__(self):
        return (f"{self.name} - Developer - ${self.salary}")

class Manager(Employee):
    def __init__(self, name, email, salary, monthly_bonus):
        super().__init__(name, email, salary)
        self.monthly_bonus = monthly_bonus

    def calculate_monthly_pay(self):
        return super().calculate_monthly_pay() + self.monthly_bonus

    def __str__(self):
        return (f"{self.name} - Manager - ${self.salary}")

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        found = self.find_employee(employee.email)
        if found is not None:
            raise ValueError("Employee already exists")
        self.employees.append(employee)

    def find_employee(self, email):
        for employee in self.employees:
            if email.lower() == employee.email.lower():
                return employee
        return None

    def remove_employee(self, email):
        found = self.find_employee(email)
        if found is None:
            raise ValueError("Employee not found")
        self.employees.remove(found)
        return found

    def total_monthly_payroll(self):
        return sum(employee.calculate_monthly_pay() for employee in self.employees)
        

        