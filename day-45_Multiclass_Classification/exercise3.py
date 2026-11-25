import torch
import torch.nn as nn

class MulticlassClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(2, 32)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(32, 32)
        self.linear3 = nn.Linear(32, 3)

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        x = self.relu(x)
        return self.linear3(x)

torch.manual_seed(42)

x = (torch.rand(3000, 2) * 6) - 3

distance_squared = x[:, 0] ** 2 + x[:, 1] ** 2
# Generate y using classification rules
mask_one = (distance_squared <= 4) & (distance_squared > 1)
mask_two = distance_squared > 4

y = torch.zeros_like(distance_squared, dtype=torch.long)
y[mask_one] = 1
y[mask_two] = 2
# Training config

learning_rate = 0.01
epochs = 3000

# Initialize model and find logit values

model = MulticlassClassifier()

# Train model 

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=learning_rate
)
criterion = nn.CrossEntropyLoss()
softmax = nn.Softmax(dim=1)

for epoch in range(epochs):
    # Clear previous gradients
    optimizer.zero_grad()
    # Forward pass
    logits = model(x)
    loss = criterion(logits, y)
    # Backward pass
    loss.backward()
    # Update parameters
    optimizer.step()
    # Print loss every 300 epochs
    if (epoch + 1) % 300 == 0:
        print(f"Epoch #{epoch + 1} -- Loss: {loss.item()}")

# Evaluate model on training data
model.eval()

with torch.no_grad():
    training_logits = model(x)
    print(f"Training logits:\n{training_logits[:5]}")
    training_probabilities = softmax(training_logits)
    print(f"Training probabilities:\n{training_probabilities[:5]}")
    training_predictions = torch.argmax(training_probabilities, dim=1)
    print("Training predictions: ", training_predictions[:5])
    row = torch.arange(0, len(training_logits))
    column = y
    selected = training_probabilities[row, column]
    print("Selected: ", selected[:5])
    training_accuracy = (training_predictions == y).float().mean().item()
    print("Training Accuracy", training_accuracy)
    print("Shape of logits: ", training_logits.shape)
    print("Shape of probabilities: ", training_probabilities.shape)
    print("Shape of predictions ", training_predictions.shape)
    print("Shape of targets: ", y.shape)

# Evaluate on testing data

torch.manual_seed(100)

x_test = (torch.rand(1000, 2) * 6) - 3

distance_squared_test = x_test[:, 0] ** 2 + x_test[:, 1] ** 2
mask_zero_test = distance_squared_test <= 1
mask_one_test = (distance_squared_test <= 4) & (distance_squared_test > 1)
mask_two_test = distance_squared_test > 4
y_test = torch.zeros_like(distance_squared_test, dtype=torch.long)
y_test[mask_one_test] = 1
y_test[mask_two_test] = 2

model.eval()

with torch.no_grad():
    test_logits = model(x_test)
    print(f"Testing logits:\n{test_logits[:5]}")
    test_probabilities = softmax(test_logits)
    print(f"Testing probabilities:\n{test_probabilities[:5]}")
    test_predictions = torch.argmax(test_probabilities, dim=1)
    print("Testing predictions: ", test_predictions[:5])
    test_row = torch.arange(0, len(test_logits))
    test_colummns = y_test
    test_selected = test_probabilities[test_row, test_colummns]
    print("Selected: ", test_selected[:5])
    manual_ce = -torch.log(test_selected)
    manual_ce_mean = manual_ce.mean()
    print("Loss: ", manual_ce_mean.item())
    test_accuracy = (test_predictions == y_test).float().mean().item()
    print("Testing accuracy: ", test_accuracy)

#Compare test and training accuracy
print("Training accuracy: ", training_accuracy)
print("Testing accuracy: ", test_accuracy)
class_zero_acc = (test_predictions[mask_zero_test] == y_test[mask_zero_test]).float().mean().item()
class_one_acc = (test_predictions[mask_one_test] == y_test[mask_one_test]).float().mean().item()
class_two_acc = (test_predictions[mask_two_test] == y_test[mask_two_test]).float().mean().item()
print("Class 0 accuracy ", class_zero_acc)
print("Class 1 accuracy: ", class_one_acc)
print("Class 2 accuracy: ", class_two_acc)















