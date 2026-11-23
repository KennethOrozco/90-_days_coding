import torch
import torch.nn as nn

logits = torch.tensor([
    [-2.0],
    [0.0],
    [2.0],
    [4.0]
])

targets = torch.tensor([
    [0.0],
    [1.0],
    [1.0],
    [0.0]
])

# Initialize nn.BCEWithLogitsLoss()
criterion = nn.BCEWithLogitsLoss()

# Calculate loss from logits and targets.
loss = criterion(logits, targets)

# Apply sigmoid to logits
sigmoid = nn.Sigmoid()

probabilities = sigmoid(logits)

print(probabilities)

# Initialize nn.BCELoss() and calculate the loss using probabilites

criterion_v2 = nn.BCELoss()

loss_v2 = criterion_v2(probabilities, targets)

# Print and compare both loss values.
print("Loss with BCEwithLogitsLoss(): ", loss)
print("Loss with BCELoss(): ", loss_v2)
if torch.isclose(loss, loss_v2):
    print("They are the same!")
else:
    print("Not the same!")

# Use a threshold of 0.5 to produce binary predictions
predictions = (probabilities >= 0.5).long()

accuracy = (predictions == targets).float().mean().item()

print("Accuracy: ", accuracy)





