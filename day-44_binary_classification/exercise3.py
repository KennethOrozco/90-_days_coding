import torch
import torch.nn as nn

class CircleClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(2, 16)
        self.relu =nn.ReLU()
        self.linear2 = nn.Linear(16, 1)

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu(x)
        return self.linear2(x)

torch.manual_seed(42)

# Generate training data
x = (torch.rand(1000, 2) * 6) - 3

# Label points inside the circle as 1
y = ((x[:, 0] ** 2 + x[:, 1] ** 2) <= 4).float()
y = y.reshape(-1, 1)

learning_rate = 0.01
epochs = 2000
# Initialize model
model = CircleClassifier()
# Initialize loss
criterion = nn.BCEWithLogitsLoss()
# Initialize SGD optimizer
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=learning_rate
)
# Train for 2,000 epochs
for epoch in range(epochs):
    # Clear previous gradients
    optimizer.zero_grad()
    #Forward pass
    predictions = model(x)
    loss = criterion(predictions, y)
    # Backward pass
    loss.backward()
    # Update parameters
    optimizer.step()
    # Print loss every 200 epochs
    if (epoch + 1) % 200 == 0:
        print(f"Epoch: {epoch + 1} -- Loss: {loss}")

# Evaluate model
sigmoid = nn.Sigmoid()
model.eval()

with torch.no_grad():
    logits = model(x)
    probabilities = sigmoid(logits)
    predictions = (probabilities >= .5).long()
    accuracy = (predictions == y).float().mean().item()
    print("Training accuracy: ", accuracy)

# Evaluate model with test data
model.eval()

with torch.no_grad():
    x_test = torch.tensor([
        [0.0, 0.0],
        [1.0, 1.0],
        [2.5, 0.0],
        [0.0, -2.5],
        [1.5, 1.5]
    ])
    test_logits = model(x_test)
    test_probabilities = sigmoid(test_logits)
    expected_labels = (x_test[:,0]**2 + x_test[:, 1] **2 <= 4).long().reshape(-1, 1)
    test_predictions = (test_probabilities >= .5).long()
    print(f"Test probabilites:\n{test_probabilities}")
    print(f"Expected labels:\n{expected_labels}")
    print(f"Test accuracy: {(test_predictions == expected_labels).float().mean().item()}")
    

