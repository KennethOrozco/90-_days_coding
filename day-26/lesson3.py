actual =    [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1]
predicted = [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1]

tp = 0
fn = 0
for label_actual, label_predicted in zip(actual, predicted):
    if label_actual == 1 and label_actual == label_predicted:
        tp += 1
    elif label_actual == 1 and label_actual != label_predicted:
        fn += 1

if tp + fn == 0:
    recall = 0.0
else:
    recall = tp / (tp + fn)

print(recall)
print(f"Recall: {recall:.2%}")

model_a_recall = 24 / (24 + 6)
model_b_recall = 18 / (18 + 2)

print(model_a_recall)
print(model_b_recall
      )
if model_a_recall > model_b_recall:
    print(f"Model A's recall is higher than Model B's")
else:
    print(f"Model B's recall is higher than Model A's")

for index, (label_actual, label_predicted) in enumerate(zip(actual, predicted), start=1):
    if label_actual == 1 and label_actual != label_predicted:
        print(f"Transacton #{index} is a false negative!")
