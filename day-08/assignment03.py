def calculate_average(scores):
    if not scores:
        return 0
    total = 0
    for score in scores:
        if score < 0:
            return None
        total += score
    return total/len(scores)
    
    