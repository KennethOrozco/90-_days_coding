import torch
import torch.nn as nn

logits = torch.tensor([
    [-3.0],
    [-1.0],
    [0.0],
    [1.0],
    [3.0]
])

sigmoid = nn.Sigmoid()

# Apply sigmoid to logits
probabilties = sigmoid(logits)
# Conver the probabilities into binary predictions using a threshold of 0.5
predictions_five = (probabilties >= 0.5).long()
print(f"Og Logits:\n{logits}")
print(f"Probabilities:\n{probabilties}")
print(f"Predictions for 0.5 threshold:\n{predictions_five}")

# binary predictions with a threshold of 0.7
predictions_seven = (probabilties >= 0.7).long()

print(f"Predictions for 0.7 threshold:\n{predictions_seven}")

