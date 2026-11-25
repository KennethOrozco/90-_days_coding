import torch
import torch.nn as nn

logits = torch.tensor([
    [2.0, 1.0, 0.0],
    [-1.0, 3.0, 1.0],
    [0.0, 0.0, 0.0],
    [4.0, 2.0, 1.0],
    [-2.0, -1.0, 2.0]
])

targets = torch.tensor([0, 1, 2, 0, 2])

# Initialize cross entropy loss
criterion = nn.CrossEntropyLoss()
# Calculate and print loss using raw logits
loss = criterion(logits, targets)
print("Loss: ", loss)

# Calculate the softmax probabilities seperately
softmax = nn.Softmax(dim=1)
probabilities = softmax(logits)
print(f"probabilities:\n{probabilities}")
# Extract the probability for each sample for the correct class
predicted_class = torch.argmax(probabilities, dim=1)
rows = torch.arange(0, len(logits))
columns = targets
selected = probabilities[rows, columns]
print(f"selected: {selected}")
print(predicted_class)
# Calculate the mean of the manual cross entropy
manual_ce = - torch.log(selected)
manual_ce_mean = manual_ce.mean()
print("Manual cross entropy: ",manual_ce_mean)
# use torchisclose() to verify the manual ce with torchs
print("Are the manual and torch's loss the same?: ", torch.isclose(loss, manual_ce_mean))
# Calculate and print the classification accuracy
classification_accuracy = (predicted_class == targets).float().mean().item()
print("Classification accuracy: ", classification_accuracy)
# Print the shape and dtype of targets.
print("Shape: ", targets.shape)
print("Data type: ", targets.dtype)