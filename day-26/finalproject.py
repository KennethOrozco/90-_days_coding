from sklearn.metrics import(
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


actual = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 1, 1, 1, 1, 1
]

model_a = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

model_b = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 1, 1, 1, 1, 1, 1, 0, 0
]

model_a_accuracy = accuracy_score(actual, model_a)
model_a_precision = precision_score(actual, model_a, zero_division=0)
model_a_recall = recall_score(actual, model_a, zero_division=0)
model_a_f1 = f1_score(actual, model_a, zero_division=0)

model_b_accuracy = accuracy_score(actual, model_b)
model_b_precision = precision_score(actual, model_b, zero_division=0)
model_b_recall = recall_score(actual, model_b, zero_division=0)
model_b_f1 = f1_score(actual, model_b, zero_division=0)

models = {
    "model_a": {
        "accuracy": model_a_accuracy,
        "precision": model_a_precision,
        "recall": model_a_recall,
        "f1": model_a_f1
    },
    "model_b": {
        "accuracy": model_b_accuracy,
        "precision": model_b_precision,
        "recall": model_b_recall,
        "f1": model_b_f1
    },
}

for (k1, v1), (k2, v2) in zip(models["model_a"].items(), models["model_b"].items()):
    if v1 > v2:
        print(f"Model A's {k1} is higher")
    elif v2 > v1:
        print(f"Model B's {k1} is higher")
    else:
        print(f"The {k1} scores are tied!")


tp = 0
tn = 0
fp= 0
fn = 0
for label_actual , label_predicted in zip(actual, model_b):
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

if abs(model_b_precision - manual_precision) < 1e-9:
    print("Precision are the same")
if abs(model_b_recall - manual_recall) < 1e-9:
    print("Recall are the same")
if abs(model_b_f1 - manual_f1) < 1e-9:
    print("F1 are the same")

for index, (label_actual, label_predicted) in enumerate(zip(actual, model_b), start=1):
    if label_actual == 1 and label_actual != label_predicted:
        print(f"Transaction #{index} is a False-Negative")
    elif label_actual == 0 and label_actual != label_predicted:
        print(f"Transactio #{index} is a False-Positive")
    