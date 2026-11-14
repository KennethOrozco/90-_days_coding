def most_common(numbers):
    if not numbers:
        return None
    else:
        list_count = {}
        for number in numbers:
            list_count[number] = list_count.get(number, 0) + 1
        max_val = max(list_count.values())
        highest_count = {number: count for number ,count in list_count.items() if count == max_val}
        return highest_count





numbers = [4, 7, 2, 9, 7, 4, 10, 2, 7, 15, 4]

print(most_common(numbers))
