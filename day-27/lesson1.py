actual = [
    0, 1, 0, 0, 1,
    1, 0, 1, 0, 1,
    0, 0, 1, 0, 1
]

predicted = [
    0, 1, 0, 1, 1,
    0, 0, 1, 0, 0,
    0, 1, 1, 0, 1
]

tp = 0
fp = 0
fn = 0
tn = 0

for label_actual, label_predicted in zip(actual, predicted):
    if label_actual == 1 and label_actual == label_predicted:
        tp += 1
    elif label_actual == 1 and label_actual != label_predicted:
        fn += 1
    elif label_actual == 0 and label_actual != label_predicted:
        fp += 1
    else:
        tn += 1

matrix = [
    [tn, fp],
    [fn, tp]
]
if not len(actual):
    accuracy = 0.0
else:
    accuracy = (tn + tp) / len(actual)

if tp + fp == 0:
    precision = 0.0
else:
    precision = tp / (tp + fp)

if tp + fn == 0:
    recall = 0.0
else:
    recall = tp / (tp + fn)

if 2 * tp + fp + fn == 0:
    f1 = 0.0
else:
    f1 = (2 * tp) / (2 * tp + fp + fn)

print("Accuracy: ", accuracy)
print("Precision: ", precision)
print("Recall: ", recall)
print("F1: ", f1)

for index , (label_actual, label_predicted) in enumerate(zip(actual, predicted), start=1):
    if label_actual == 0 and label_actual != label_predicted:
        print(f"Transaction #{index} was a False-Positive!")
    if label_actual == 1 and label_actual != label_predicted:
        print(f"Transaction #{index} was a False-Negative!")

print(f"{matrix[0]}\n{matrix[1]}")