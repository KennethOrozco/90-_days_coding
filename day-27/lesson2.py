from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

actual = [
    0, 1, 0, 1, 1,
    0, 0, 1, 0, 1,
    0, 1, 0, 0, 1
]

predicted = [
    0, 1, 1, 1, 0,
    0, 0, 1, 0, 0,
    1, 1, 0, 0, 1
]

matrix = confusion_matrix(actual, predicted, labels=[0, 1])
print(matrix)

tn, fp, fn, tp = matrix.ravel()

print("TN: ", tn)
print("FP: ", fp)
print("FN: ", fn)
print("TP: ", tp)

tp_manual = 0
fp_manual = 0
fn_manual= 0
tn_manual = 0

for label_actual, label_predicted in zip(actual, predicted):
    if label_actual == 1 and label_actual == label_predicted:
        tp_manual += 1
    elif label_actual == 1 and label_actual != label_predicted:
        fn_manual += 1
    elif label_actual == 0 and label_actual != label_predicted:
        fp_manual += 1
    else:
        tn_manual += 1

if abs(tn - tn_manual) < 1e-9:
    print("TN is the same")
if abs(fp - fp_manual) < 1e-9:
    print("FP is the same")
if abs(fn - fn_manual) < 1e-9:
    print("FN is the same")
if abs(tp - tp_manual) < 1e-9:
    print("TP is the same")

accuracy = accuracy_score(actual, predicted)
precision = precision_score(actual, predicted)
recall = recall_score(actual, predicted)
f1 = f1_score(actual, predicted)

if not len(actual):
    accuracy_manual = 0.0
else:
    accuracy_manual = (tp + tn) / len(actual)

if tp + fp == 0:
    precision_manual = 0.0
else:
    precision_manual = tp / (tp + fp)

if tp + fn == 0:
    recall_manual = 0.0
else:
    recall_manual = tp / (tp + fn)

if precision_manual + recall_manual == 0:
    f1_manual = 0.0
else:
    f1_manual = 2 * precision_manual * recall_manual / (precision_manual + recall_manual)

if abs(accuracy - accuracy_manual) < 1e-9:
    print("Accuracy is the same")
if abs(precision - precision_manual) < 1e-9:
    print("Precision is the same")
if abs(recall - recall_manual) < 1e-9:
    print("Recall is the same")
if abs(f1 - f1_manual) < 1e-9:
    print("F1 is the same")
