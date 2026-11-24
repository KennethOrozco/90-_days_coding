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
# Initialize Softmax and apply to logits
softmax = nn.Softmax(dim=1)

probabilities = softmax(logits)

print(f"logits:\n{logits}")
print(f"Probabilities:\n{probabilities}")
# Verify sum of sample equals 1
print(probabilities.sum(dim=1))
predicted_class = torch.argmax(probabilities, dim=1)    
# Obtain predicted classes from logits and compare results
print("Predicted class: ", predicted_class)
predicted_class_logits = torch.argmax(logits, dim=1)
print("Predicted class with logits: ", predicted_class_logits)
print("Actual class: ", targets)
# Calculate classification accuracy using targets
probabilities_accuracy = (predicted_class == targets).float().mean().item()
print("Probabilities accuracy: ", probabilities_accuracy)
logits_accuracy = (predicted_class_logits == targets).float().mean().item()
print("Logits accuracy: ", logits_accuracy)
# Print shapes
print(f"Shapes: -- logits: {logits.shape} -- probabilities: {probabilities.shape} -- predictions: {predicted_class.shape} -- targets: {targets.shape}") 
