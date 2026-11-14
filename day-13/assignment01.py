# def calculate_average(scores:list[int]) -> float:
#     if not scores:
#         return 0

#     return float(sum(scores) / len(scores))

# def find_score(scores:dict[str, int], name:str) -> int | None:
#     if name not in scores:
#         return None

#     return scores[name]
def add_score(students:dict[str, list[int]], name:str, score:int) -> None:
    if name not in students:
        students[name] = []

    students[name].append(score)