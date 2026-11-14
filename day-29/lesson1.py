def majority_vote(predictions: list[int]) -> int | None:
    if not predictions:
        return None
    count_one = sum(predictions)
    count_zero = predictions.count(0)
    if count_one > count_zero:
        return 1
    return 0

def forest_predict(tree_predictions: dict[str, list[int]]) -> list[int] | None:
    if not tree_predictions:
        return None
    final_prediction = []

    for predictions in zip(*tree_predictions.values()):
        final_prediction.append(majority_vote(predictions))

    return final_prediction


def calculate_accuracy(predictions: list[int], actual_labels: list[int]) -> float:
    if not predictions or not actual_labels:
        raise  ValueError("There are no predictions and/or labels.")
    correct = 0
    if len(predictions) != len(actual_labels):
        raise ValueError("Predictions and actual labesl must be the same length.")
    for index, prediction in enumerate(predictions):
        if prediction == actual_labels[index]:
            correct += 1

    return correct / len(predictions)

def ensemble_evaluation(forest_tree_accuracy: float, data: dict[float]) -> None:
    better = 0
    worse = 0
    equal = 0
    for accuracy in data:
        if forest_tree_accuracy > data[accuracy]:
            better += 1
        elif forest_tree_accuracy < data[accuracy]:
            worse +=1
        else:
            equal += 1
    print(f"Better: {better} -- Worse: {worse} -- Equal: {equal}")
        




tree_predictions = {
    "tree_1": [1, 0, 1, 1, 0],
    "tree_2": [1, 1, 1, 0, 0],
    "tree_3": [0, 0, 1, 1, 0],
    "tree_4": [1, 0, 0, 1, 0],
    "tree_5": [1, 1, 1, 1, 1]
}

actual_labels = [1, 0, 1, 0, 0]
forest_predictions = forest_predict(tree_predictions)
print("Forest Tree Predictions: ", forest_predictions)
print("Actual Labels: ", actual_labels)

forest_tree_accuracy = calculate_accuracy(forest_predictions, actual_labels)
print("Forest Tree Accuracy: ", forest_tree_accuracy)

data = {}

for prediction in tree_predictions:
    accuracy = calculate_accuracy(tree_predictions[prediction], actual_labels)
    data[prediction] = accuracy

print(data)

ensemble_evaluation(forest_tree_accuracy, data)











