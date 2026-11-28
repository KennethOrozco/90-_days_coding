import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

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

# Generate training labels

y = torch.zeros_like(distance_squared, dtype=torch.long)

mask_class_one = (distance_squared > 1) & (distance_squared <= 4)
mask_class_two = distance_squared > 4

y[mask_class_one] = 1
y[mask_class_two] = 2

learning_rate = 0.01
epochs = 100

print("Class Distribution: ", torch.bincount(y, minlength=3))

# Create dataset and data loader

dataset = TensorDataset(x, y)

loader = DataLoader(
    dataset,
    batch_size=64,
    shuffle=True
)

# Initialize model and optimizer

model = MulticlassClassifier()

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=learning_rate
)

criterion = nn.CrossEntropyLoss()

# Train using mini batches

optimizer_step_count = 0
for epoch in range(epochs):
    running_loss = 0
    for batch_x, batch_y in loader:
        optimizer.zero_grad()
        logits = model(batch_x)
        loss = criterion(logits, batch_y)
        loss.backward()
        optimizer.step()
        running_loss += loss.item() * len(batch_x)
        optimizer_step_count += 1
    if (epoch + 1) % 10 == 0:    # Print epoch loss every 10 epochs
        epoch_loss = running_loss / len(dataset)
        print(f"Epoch {epoch + 1} Loss: {epoch_loss}")

print("Optimizer step count: ", optimizer_step_count)
# Calculate the final training accuracy

model.eval()

with torch.no_grad():
    training_logits = model(x)
    training_predictions = torch.argmax(training_logits, dim=1)
    training_accuracy = (training_predictions == y).float().mean().item()
    print("Final training accuracy: ", training_accuracy)

# Evaluate with randomly generated test data

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
    test_loss = criterion(test_logits, y_test)
    test_predictions = torch.argmax(test_logits, dim=1)
    test_accuracy = (test_predictions == y_test).float().mean().item()
    print("Test Loss: ", test_loss)
    print("Test Accuracy: ", test_accuracy)

# Calculate accuracy for each class

class_zero_acc = (test_predictions[mask_zero_test] == y_test[mask_zero_test]).float().mean().item()
class_one_acc = (test_predictions[mask_one_test] == y_test[mask_one_test]).float().mean().item()
class_two_acc = (test_predictions[mask_two_test] == y_test[mask_two_test]).float().mean().item()
print("Class 0 accuracy ", class_zero_acc)
print("Class 1 accuracy: ", class_one_acc)
print("Class 2 accuracy: ", class_two_acc)


