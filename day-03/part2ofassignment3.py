def convert_to_int(integers):
    numbers = list(map(int,integers.split()))
    return numbers

def analyze_numbers(numbers):
    total = len(numbers)
    sum_ = sum(numbers)
    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    data = {
        "Total": total,
        "Sum": sum_,
        "Largest": largest,
        "Smallest": smallest
    }
    return data

try:
    file_path = "numbers.txt"
    with open(file_path, "r") as file:
        content = file.read()
        list_of_integers = convert_to_int(content)
        result = analyze_numbers(list_of_integers)
        for key, value in result.items():
            print(f"{key}: {value}")
except FileNotFoundError:
    print("This file does not exist.")
    
    




