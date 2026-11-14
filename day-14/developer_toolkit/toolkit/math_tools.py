def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def find_max(numbers: list[float]) -> float | None:
    if not numbers:
        return None
    return max(numbers)
