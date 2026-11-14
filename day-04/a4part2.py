def analyze_duplicates(numbers):
    list_count = {}
    for number in numbers:
        list_count[number] = list_count.get(number, 0) + 1
    duplicates = {number:count for number, count in list_count.items() if count >= 2}
    return duplicates




numbers = [5, 2, 8, 5, 3, 8, 8, 1, 5, 10, 3]

print(analyze_duplicates(numbers))