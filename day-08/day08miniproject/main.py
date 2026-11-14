import expense_manager

file_path = r"C:\Users\koroz\90-days-coding\day-08\day08miniproject\expenses.json"

expenses = expense_manager.load_expenses(file_path)

while True:
    options = {
        1: "View Expenses",
        2: "Add Expense",
        3: "View total Spending",
        4: "View Category Summary",
        5: "View Highest Expense",
        6: "Filter by Category",
        7: "Exit"
    }
    for key, value in options.items():
        print(f"{key}. {value}")
    option = input("Choose the number that corresponds to the option you would like to select: ")
    if option == "1":
        print(expenses)
    elif option == "2":
        description = input("What is the descripton of the expense you would like to add?: ")
        category = input("What is it's category?: ")
        while True:
            try:
                amount = float(input("What is it's amount?: "))
                break
            except ValueError:
                print("type a float!")
        expense = expense_manager.create_expense(description, category, amount)
        if expense:
            expense_manager.add_expense(expenses, expense)
            expense_manager.save_expenses(expenses, file_path)
            print('Expense was added!')
        else:
            print('Expense was not added!')
    elif option == "3":
        print(expense_manager.total_spending(expenses))
    elif option == "4":
        print(expense_manager.category_summary(expenses))
    elif option == "5":
        print(expense_manager.highest_expense(expenses))
    elif option == "6":
        while True:
            category = input("Type the category you would like to filter: ")
            if category.strip():
                break
            else:
                print("Type a category!")

        print(expense_manager.filter_by_category(expenses, category))
    elif option == "7":
        break
    else:
        print("Invalid option!")
