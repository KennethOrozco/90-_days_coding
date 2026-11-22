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

class LinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(1, 16)
        self.linear2 = nn.Linear(16, 16)
        self.linear3 = nn.Linear(16, 1)

    
    def forward(self, x):
        x = self.linear1(x)
        x = self.linear2(x)
        return self.linear3(x)

def train_model(model: nn.Module, x: torch.Tensor, y: torch.Tensor, learning_rate: float, epochs: int) -> float:
    optimizer = torch.optim.SGD(
        model.parameters(),
        lr=learning_rate
    )
    criterion = nn.MSELoss()
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
    model.eval()
    with torch.no_grad():
        predictions = model(x)
        final_loss = criterion(predictions, y)
    return final_loss.item()
    

torch.manual_seed(42)

x = torch.linspace(-5, 5, 101).reshape(-1, 1)
y = x ** 2

learning_rate = 0.001
epochs = 2000

# Initialize model
model_a= NonlinearModel()

torch.manual_seed(42)

model_b = LinearModel()

model_a_loss = train_model(model_a, x, y, learning_rate, epochs)
model_b_loss = train_model(model_b, x, y, learning_rate, epochs)

print("Model A loss: ", model_a_loss)
print("Model B loss ", model_b_loss)

x_test = torch.tensor([
    [-4.55],
    [-2.35],
    [0.55],
    [2.65],
    [4.85]
])

y_test = x_test ** 2

criterion = nn.MSELoss()

model_a.eval()

with torch.no_grad():
    test_predictions_a = model_a(x_test)
model_a_test_loss = criterion(test_predictions_a, y_test)
print("Model A test loss: ", model_a_test_loss)

model_b.eval()

with torch.no_grad():
    test_predictions_b = model_b(x_test)
model_b_test_loss = criterion(test_predictions_b, y_test)
print("Model B test loss: ", model_b_test_loss)
    





