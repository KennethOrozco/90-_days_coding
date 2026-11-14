numbers = [3, 7, 10, 12, 15, 18, 21,24]

doubled = [number*2 for number in numbers]

even_numbers = [number for number in numbers if number % 2 == 0]

large_numbers = [number for number in numbers if number > 12]

even_squares = [number ** 2 for number in numbers if number % 2 == 0] 

print(doubled)

print(even_numbers)

print(large_numbers)

print(even_squares)
