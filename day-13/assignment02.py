class Company:
    def __init__(self, name:str) -> None:
        self.name:str = name
        self.employees:list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def find_employee(self, email:str) -> Employee | None:
        for employee in self.employees:
            if employee.email.lower() == email.lower():
                return employee
        return None

class Employee:
    def __init__(self, name: str, email: str, salary: float):
        self.name = name
        self.email = email
        self.salary = salary