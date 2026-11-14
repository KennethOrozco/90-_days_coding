actual =    [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1]
predicted = [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]

tp = 0
fp= 0

for label_actual , label_predicted in zip(actual, predicted):
    if label_actual == 1 and label_predicted == 1:
        tp += 1
    elif label_actual == 0 and label_actual != label_predicted:
        fp += 1

if tp + fp == 0:
    precision = 0.0
else:
    precision = tp / (tp + fp)

print(precision)
print(f"Precision: {precision:.2%}")

model_a_precision = 18 / (18 + 2)
model_b_precision = 12 / (12 + 1)

if model_a_precision > model_b_precision:
    print(f"Model A is more precise: {model_a_precision:.2%}")
else:
    print(f'Model B is more precise: {model_b_precision:.2%}')