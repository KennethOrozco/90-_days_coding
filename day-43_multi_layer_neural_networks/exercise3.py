import torch
import torch.nn as nn

class NonlinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(1, 16)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(16, 16)
        self.linear3 = nn.Linear(16, 1)

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        x = self.relu(x)
        return self.linear3(x)

torch.manual_seed(42)

x = torch.linspace(-5, 5, 101).reshape(-1, 1)
y = x ** 2

learning_rate = 0.001
epochs = 2000

# Initialize model
model = NonlinearModel()

# Initialize MSE loss function
criterion = nn.MSELoss()

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=learning_rate
)

# Train the model for 2,000 epochs
for epoch in range(epochs):
    #Clear previous gradients
    optimizer.zero_grad()
    # Forward pass
    predictions = model(x)
    loss = criterion(predictions, y)
    # Backward pass
    loss.backward()
    #Update parameters
    optimizer.step()
    if (epoch + 1) % 200 == 0:
        print("Epoch: ", epoch + 1)
        print("Loss: ", loss)

model.eval()

with torch.no_grad():
    x_test = torch.tensor([
        [-4.5],
        [-2.5],
        [0.5],
        [2.5],
        [4.5]
        ])
    y_test = x_test ** 2
    test_predictions = model(x_test)
    print(f"Predictions:\n{test_predictions}")
    print(f"Expected:\n{y_test}")
    
    
