from sklearn.metrics import(
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

actual = [0, 0, 1, 0, 1, 1, 0, 1, 0, 1]

probabilities = [
    0.05, 0.20, 0.45, 0.35, 0.65,
    0.80, 0.55, 0.90, 0.15, 0.70
]

thresholds = [0.30, 0.50, 0.70]

data = {}

for threshold in thresholds:
    predictions = [1 if probability >= threshold else 0 for probability in probabilities]
    data[threshold] = predictions


at_three = data[0.3]
at_five = data[0.5]
at_seven = data[0.7]

accuracy_three = accuracy_score(actual, at_three)
precision_three = precision_score(actual, at_three, zero_division=0)
recall_three = recall_score(actual, at_three, zero_division=0)
f1_three = f1_score(actual, at_three, zero_division=0)

print("Accuracy score at threshold 0.3: ", accuracy_three)
print("Precision score at threshold 0.3: ", precision_three)
print("Recall score at threshold 0.3: ", recall_three)
print("F1 score at threshold 0.3: ", f1_three)

accuracy_five = accuracy_score(actual, at_five)
precision_five = precision_score(actual, at_five, zero_division=0)
recall_five = recall_score(actual, at_five, zero_division=0)
f1_five = f1_score(actual, at_five, zero_division=0)

print("Accuracy score at threshold 0.5: ", accuracy_five)
print("Precision score at threshold 0.5: ", precision_five)
print("Recall score at threshold 0.5: ", recall_five)
print("F1 score at threshold 0.5: ", f1_five)

accuracy_seven = accuracy_score(actual, at_seven)
precision_seven = precision_score(actual, at_seven, zero_division=0)
recall_seven = recall_score(actual, at_seven, zero_division=0)
f1_seven = f1_score(actual, at_seven, zero_division=0)

print("Accuracy score at threshold 0.7: ", accuracy_seven)
print("Precision score at threshold 0.7: ", precision_seven)
print("Recall score at threshold 0.7: ", recall_seven)
print("F1 score at threshold 0.7: ", f1_seven)


matrix_at_three = confusion_matrix(actual, at_three, labels=[0, 1])
matrix_at_five = confusion_matrix(actual, at_five, labels=[0, 1])
matrix_at_seven = confusion_matrix(actual, at_seven, labels=[0, 1])

print(f"Matrix at threshold 0.3:\n{matrix_at_three}")
print(f"Matrix at threshold 0.5:\n{matrix_at_five}")
print(f"Matrix at threshold 0.7:\n{matrix_at_seven}")

metrics = {
    0.3: {
        "precision": precision_three,
        "recall": recall_three,
        "f1": f1_three
    },
    0.5: {
        "precision": precision_five,
        "recall": recall_five,
        "f1": f1_five
    },
    0.7: {
        "precision": precision_seven,
        "recall": recall_seven,
        "f1": f1_seven
    }
}

for metric in metrics[0.3].keys():
    max_val = max(metrics[threshold][metric] for threshold in metrics)
    highest_threshold = [threshold for threshold in metrics if metrics[threshold][metric] == max_val]
    print(f"Highest {metric} score: {highest_threshold}")


    





