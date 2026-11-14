from employee_manager import Employee, Developer, Manager, Company

company = Company("TechCorp")

company.add_employee(
    Developer("Alex", "alex@example.com", 72000)
)

company.add_employee(
    Manager("Jordan", "jordan@example.com", 90000, 1000)
)

while True:
    options = {
        1: "View Employees",
        2: "Add Developer",
        3: "Add Manager",
        4: "Remove Employee",
        5: "Find Employee",
        6: "View Monthly Payroll",
        7: "Exit"
    }
    for key, value in options.items():
        print(f"{key}. {value}")
    option = input("Option: ")
    if option == "1":
        for employee in company.employees:
            print(employee)
    elif option == "2":
        while True:
            name = input("Name: ")
            if name.strip():
                break
            print("Type a name!")
        while True:
            email = input("Email: ")
            if email.strip():
                break
            print("Type an email!")
        while True:
            try:
                salary = float(input("Salary: "))
                break
            except ValueError:
                print("Type a float!")
        try:
            company.add_employee(Developer(name, email, salary))
        except ValueError as error:
            print(error)
        else:
            print("Developer was added!")
    elif option == "3":
        while True:
            name = input("Name: ")
            if name.strip():
                break
            print("Type a name!")
        while True:
            email = input("Email: ")
            if email.strip():
                break
            print("Type an email!")
        while True:
            try:
                salary = float(input("Salary: "))
                break
            except ValueError:
                print("Type a float!")
        while True:
            try:
                monthly_bonus = float(input("Monthly Bonus: "))
                break
            except ValueError:
                print("Type a float!")
            
        try:
            company.add_employee(Manager(name, email, salary, monthly_bonus))
        except ValueError as error:
            print(error)
        else:
            print("Manager was added!")
    elif option == "4":
        while True:
            email = input("Email: ")
            if email.strip():
                break
            print("Type an email!")
        try:
            company.remove_employee(email)
        except ValueError as error:
            print(error)
        else:
            print("Employee has been removed!")
    elif option == "5":
        while True:
            email = input("Email: ")
            if email.strip():
                break
            print("Type an email")
        found = company.find_employee(email)
        if found is None:
            print("Employee not found")
        else:
            print(found)
    elif option == "6":
        total = company.total_monthly_payroll()
        print(f"Total: {total}")
    elif option == "7":
        break
    else:
        print("Invalid option!")


        
    
