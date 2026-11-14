from pathlib import Path

MAIN_FOLDER = Path(__file__).resolve().parent
def load_numbers(file_path):
    if not file_path:
        print("There is no file path.")
        return []
    try:
        numbers = []
        path_obj = Path(file_path)
        final_path = path_obj if path_obj.is_absolute() else MAIN_FOLDER / path_obj
        with open(final_path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    numbers.append(int(line))
                except ValueError:
                    print(".txt file contained a string.")
                    continue
    except FileNotFoundError:
        print("File  was not found.")
        return []
    return numbers
        

                            
def basic_stats(numbers):
    if not numbers:
        print("There is no number to retrieve data from")
        return
    count = len(numbers)
    sum_ = sum(numbers)
    average = sum_/count
    minimum = min(numbers)
    maximum = max(numbers)
    dictionary = {
        "count": count,
        "sum": sum_,
        "average": average,
        "minimum": minimum,
        "maximum": maximum
        }
    return dictionary
    
    

def frequency(numbers):
    list_of_count = {}
    for number in numbers:
        list_of_count[number] = list_of_count.get(number, 0) + 1
    return list_of_count


def find_duplicates(numbers):
    count = frequency(numbers)
    duplicates = {key:value for key, value in count.items() if value >= 2}
    return duplicates


def filter_numbers(numbers, minimum):
    filtered = [number for number in numbers if number >= minimum]
    return filtered





