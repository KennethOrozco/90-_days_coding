actual =    [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1]
predicted = [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]

tp = 0
tn = 0
fp= 0
fn = 0
for index, (label_actual , label_predicted) in enumerate(zip(actual, predicted), start=1):
    if label_actual == 1 and label_predicted == 1:
        tp += 1
    elif label_actual == 0 and label_predicted == 0:
        tn += 1
    elif label_actual == 0 and label_actual != label_predicted:
        fp += 1
        print(f"Transaction #{index} predicted incorrectly!")
    elif label_actual == 1 and label_actual != label_predicted:
        fn += 1
        print(f"Transaction #{index} predicted incorrectly!")

print(tp)
print(tn)
print(fp)
print(fn)

accuracy = (tp + tn) / (tp + tn + fp + fn)
print(accuracy)
print(f"Accuracy: {accuracy:.2%}")
