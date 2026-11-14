import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

#Function that retrurns a dictionary of metrics
def evaluate_model(predictions: np.array, y : np.array) -> dict[str, float]:
    return {
        "accuracy": accuracy_score(y, predictions),
        "precision": precision_score(y, predictions, zero_division=0),
        "recall": recall_score(y, predictions, zero_division=0),
        "f1": f1_score(y, predictions, zero_division=0)
    }

y_true = np.array([
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    1, 1, 1, 1, 1
])

model_a_predictions = np.array([
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0
])

model_b_predictions = np.array([
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 1, 1,
    1, 1, 1, 0, 0
])

#Evaluate model for their metrics.
model_a_data = evaluate_model(model_a_predictions, y_true)
model_b_data = evaluate_model(model_b_predictions, y_true)

# Get each modes matrix and extract tn, fp, fn, and tp
model_a_matrix = confusion_matrix(y_true, model_a_predictions, labels=[0, 1])
model_b_matrix = confusion_matrix(y_true, model_b_predictions, labels=[0, 1])

model_a_tn, model_a_fp, model_a_fn, model_a_tp = model_a_matrix.ravel()
model_b_tn, model_b_fp, model_b_fn, model_b_tp = model_b_matrix.ravel()

print("Model A TN: ", model_a_tn)
print("Model A FP: ", model_a_fp)
print("Model A FN: ", model_a_fn)
print("Model A TP: ", model_a_tp)

print("Model B TN: ", model_b_tn)
print("Model B FP: ", model_b_fp)
print("Model B FN: ", model_b_fn)
print("Model B TP: ", model_b_tp)

#Print classificaton report for both models

class_report_a = classification_report(y_true, model_a_predictions, zero_division=0)
class_report_b = classification_report(y_true, model_b_predictions, zero_division=0)

print(class_report_a)
print(class_report_b)

model_a_class_one_f1 = f1_score(y_true, model_a_predictions, pos_label=1, zero_division=0)
model_b_class_one_f1 = f1_score(y_true, model_b_predictions, pos_label=1, zero_division=0)

if model_a_class_one_f1 > model_b_class_one_f1:
    print(f"Model A F1: {model_a_class_one_f1}")
elif model_b_class_one_f1 > model_a_class_one_f1:
    print(f"Model B F1: {model_b_class_one_f1}")
else:
    print("Same F1 score!")




