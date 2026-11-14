from toolkit import calculate_average, find_max, count_words, reverse_text, is_valid_age, is_valid_email

def main() -> None:
    while True:
        options = {
            1: "Calculate Average",
            2: "Find Maximum",
            3: "Count Words",
            4: "Reverse Text",
            5: "Validate Age",
            6: "Validate Email",
            7: "Exit"
        }
        for key, value in options.items():
            print(f"{key}. {value}")
        option = input("Option: ")
        if option == "1":
            numbers = get_numbers()
            print(calculate_average(numbers))
        elif option == "2":
                numbers = get_numbers()
                print(find_max(numbers))
        elif option == "3":
             text = input("Text: ")
             print(f"Count: {count_words(text)}")
        elif option == "4":
             text = input("Text: ")
             print(reverse_text(text))
        elif option == "5":
            while True:
                try:
                    age = int(input("Age: "))
                    break
                except ValueError:
                     print("Type an integer!")
            print(is_valid_age(age))
        elif option == "6":
            email = input("Email: ")
            print(is_valid_email(email))
        elif option == "7":
             break
        else:
             print("Invalid option!")

            
                


def get_numbers() -> list[float]:
     while True:
        try:
            user_input = input("Type a list of numbers: ")
            numbers = [float(number) for number in user_input.split()]
            if not numbers:
                raise ValueError("Enter at least one number!")
        except ValueError as error:
                print(error)
        else:
            return numbers

    

            
if __name__ == "__main__":
    main()