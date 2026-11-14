def get_numbers():
    numbers = [4, 8, 15, 16, 23, 42]
    return numbers


def analyze_numbers(numbers):
    total = len(numbers)
    sum_ = sum(numbers)
    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    data = {
        "Total": total,
        "Sum": sum_,
        "Largest": largest,
        "Smallest": smallest
    }

    return data


def display_result(result):


    for key, value in result.items():
        print(f"{key}: {value}")


analyzed_data = analyze_numbers(get_numbers())

display_result(analyzed_data)