def calculate_f1(precision: float, recall: float) -> float:
    if precision + recall == 0:
        return 0.0
    return (2 * precision * recall) / (precision + recall)

actual =    [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0]
predicted = [1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0]

tp = 0
fp = 0
fn = 0
for label_actual, label_predicted in zip(actual, predicted):
    if label_actual == 1 and label_actual == label_predicted:
        tp += 1
    elif label_actual == 0 and label_actual != label_predicted:
        fp += 1
    elif label_actual == 1 and label_actual != label_predicted:
        fn += 1

if tp + fp == 0:
    precision = 0.0
else:
    precision = tp / (tp + fp)

if tp + fn == 0:
    recall = 0.0
else:
    recall = tp / (tp + fn)

if precision + recall == 0:
    f1_v1 = 0.0
else:
    f1_v1 = (2 * precision * recall) / (precision + recall)

if 2 * tp + fp + fn == 0:
    f1_v2 = 0
else:
    f1_v2 = 2 * tp / (2 * tp + fp + fn)

print("TP: ", tp)
print("FP: ", fp)
print("FN: ", fn)
print("Precision: ", precision)
print("Recall: ", recall)
print("F1 Score Version 1: ", f1_v1)
print("F1 Score Version 2: ", f1_v2)

model_a_f1 = (2 * 0.95 * 0.40) / (0.95 + 0.40)
model_b_f1 = (2 * 0.75 * 0.75) / (0.75 + 0.75)

print("Model A: ", model_a_f1)
print("Model B: ", model_b_f1)

if model_a_f1 > model_b_f1:
    print("Model A's F1 score is higher than Model B's")
else:
    print("Model B's F1 score is higher than Model A's")

print(f"F1 Function test for Model A: {calculate_f1(0.95, 0.40)}")

print(f"F1 Function test for Model B: {calculate_f1(0.75, 0.75)}")