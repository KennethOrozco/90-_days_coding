import torch
import torch.nn as nn

class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

# Create instance of model
model = LinearRegressionModel()

x = torch.tensor([
    [1.],
    [2.],
    [3.],
    [4.],
    [5.]
])

y = torch.tensor([
    [3.],
    [5.],
    [7.],
    [9.],
    [11.]
])

learning_rate = 0.01
epochs = 300

# Create SGD optimizer
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=learning_rate
)

criterion = nn.MSELoss()
# Train for 300 epochs
for epoch in range(epochs):
    # Clear previous gradients
    optimizer.zero_grad()
    # Forward pass using MSE loss
    predictions = model(x)
    loss = criterion(predictions, y)
    # Backward pass
    loss.backward()
    # Update parameters
    optimizer.step()
    if (epoch +1) % 50 == 0:
        print("Epoch: ", epoch + 1)
        print("Loss: ", loss)
     
for name, parameter in model.named_parameters():
    print(name, parameter.item())