import analyzer

def main():
    file_path = "numbers.txt"
    numbers = analyzer.load_numbers(file_path)
    choices = {
        1: "View All Numbers",
        2: "View Basic Statistics",
        3: "View Frequencies",
        4: "View Duplicates",
        5: "Filter Numbers",
        6: "Exit"
    }
    while True:
        for key, value in choices.items():
            print(f"{key}. {value}")
        choice = input("Choose an option by typing the number assigned: ")
        if choice == "1":
            print(numbers)
        elif choice == "2":
            print(analyzer.basic_stats(numbers))
        elif choice == "3":
            print(analyzer.frequency(numbers))
        elif choice == "4":
            print(analyzer.find_duplicates(numbers))
        elif choice == "5":
            try:
                minimum = int(input("Choose a minimum number: "))
                print(analyzer.filter_numbers(numbers, minimum))
            except ValueError:
                print("Type an integer!")
        elif choice == "6":
            break
        else:
            print("Not a valid choice!")




main()






