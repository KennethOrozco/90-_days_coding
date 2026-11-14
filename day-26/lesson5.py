from sklearn.metrics import(
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

actual = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 1, 1
]

model_a_predictions = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

model_b_predictions = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 1, 1, 1
]

model_a_accuracy = accuracy_score(actual, model_a_predictions)
model_a_precision = precision_score(actual, model_a_predictions, zero_division=0)
model_a_recall = recall_score(actual, model_a_predictions, zero_division=0)
model_a_f1 = f1_score(actual, model_a_predictions, zero_division=0)

print("Model A's Accuracy: ", model_a_accuracy)
print("Model A's Precision: ", model_a_precision)
print("Model A's Recall: ", model_a_recall)
print("Model A's F1: ", model_a_f1)

model_b_accuracy = accuracy_score(actual, model_b_predictions)
model_b_precision = precision_score(actual, model_b_predictions, zero_division=0)
model_b_recall = recall_score(actual, model_b_predictions, zero_division=0)
model_b_f1 = f1_score(actual, model_b_predictions, zero_division=0)

print("Model B's Accuracy: ", model_b_accuracy)
print("Model B's Precision: ", model_b_precision)
print("Model B's Recall: ", model_b_recall)
print("Model B's F1: ", model_b_f1)

if model_a_accuracy > model_b_accuracy:
    print("Model A's accuracy is better")
else:
    print("Model B's accuracy is better")

if model_a_precision > model_b_precision:
    print("Model A's precision is better")
else:
    print("Model B's precision is better")

if model_a_recall > model_b_recall:
    print("Model A's recall is better")
else:
    print("Model B's recall is better")

if model_a_f1 > model_b_f1:
    print("Model A's F1 is better")
else:
    print("Model B's F1 is better")

tp = 0
tn = 0
fp= 0
fn = 0
for label_actual , label_predicted in zip(actual, model_b_predictions):
    if label_actual == 1 and label_predicted == 1:
        tp += 1
    elif label_actual == 0 and label_predicted == 0:
        tn += 1
    elif label_actual == 0 and label_actual != label_predicted:
        fp += 1
    elif label_actual == 1 and label_actual != label_predicted:
        fn += 1

if tp + fp == 0:
    manual_precision = 0.0
else:
    manual_precision = tp / (tp + fp)

if tp + fn == 0:
    manual_recall = 0.0
else:
    manual_recall = tp / (tp + fn)

if manual_precision + manual_recall == 0:
    manual_f1 = 0.0
else:
    manual_f1 = (2 * manual_precision * manual_recall) / (manual_precision + manual_recall)

print("Manual Precison for Model B: ", manual_precision)
print("Manual Recall for Model B: ", manual_recall)
print("Manual F1 for Model B: ", manual_f1)

if abs(model_b_precision - manual_precision) < 1e-9:
    print("Precision are the same")
if abs(model_b_recall - manual_recall) < 1e-9:
    print("Recall are the same")
if abs(model_b_f1 - manual_f1) < 1e-9:
    print("F1 are the same")

