import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
import time

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

def train_model(
    model: nn.Module,
    loader: DataLoader,
    learning_rate: float,
    epochs: int
) -> dict:
    optimizer = torch.optim.SGD(
    model.parameters(),
    lr=learning_rate
)
    criterion = nn.CrossEntropyLoss()
    optimizer_step_count = 0
    model.train()
    start = time.perf_counter()
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
        epoch_loss = running_loss / len(loader.dataset)
    end = time.perf_counter()
    return {
        "final_loss": epoch_loss,
        "optimizer_steps": optimizer_step_count,
        "training_time": end - start
    }

def evaluate_model(
    model: nn.Module,
    x: torch.Tensor,
    y: torch.Tensor
) -> dict:
    criterion = nn.CrossEntropyLoss()
    model.eval()
    with torch.no_grad():
        logits = model(x)
        loss = criterion(logits, y)
        pred = torch.argmax(logits, dim=1)
        accuracy = (pred == y).float().mean().item()
        return {
            "loss": loss.item(),
            "accuracy": accuracy
        }

torch.manual_seed(42)

x = (torch.rand(3000, 2) * 6) - 3

distance_squared = x[:, 0] ** 2 + x[:, 1] ** 2

# Generate training labels

y = torch.zeros_like(distance_squared, dtype=torch.long)

mask_class_one = (distance_squared > 1) & (distance_squared <= 4)
mask_class_two = distance_squared > 4

y[mask_class_one] = 1
y[mask_class_two] = 2

dataset = TensorDataset(x, y)

learning_rate = 0.01
epochs = 100

print("Class Distribution: ", torch.bincount(y, minlength=3))

# Create three DataLoaders with batch sizes 3000, 64, 16

loader_a = DataLoader(
    dataset,
    batch_size=3000,
    shuffle=True
)

loader_b = DataLoader(
    dataset,
    batch_size=64,
    shuffle=True
)

loader_c = DataLoader(
    dataset,
    batch_size=16,
    shuffle=True
)

# Initialize models

torch.manual_seed(42)
model_a = MulticlassClassifier()

torch.manual_seed(42)
model_b = MulticlassClassifier()

torch.manual_seed(42)
model_c = MulticlassClassifier()

# Train all 3 independently

model_a_trained = train_model(model_a, loader_a, learning_rate, epochs)
print(model_a_trained)

model_b_trained = train_model(model_b, loader_b, learning_rate, epochs)
print(model_b_trained)

model_c_trained = train_model(model_c, loader_c, learning_rate, epochs)
print(model_c_trained)

# Evaluate training data

model_a_train_data = evaluate_model(model_a, x, y)

model_b_train_data = evaluate_model(model_b, x, y)

model_c_train_data = evaluate_model(model_c, x, y)

# Generate test data

torch.manual_seed(100)

x_test = (torch.rand(1000, 2) * 6) - 3

distance_squared_test = x_test[:, 0] ** 2 + x_test[:, 1] ** 2
mask_zero_test = distance_squared_test <= 1
mask_one_test = (distance_squared_test <= 4) & (distance_squared_test > 1)
mask_two_test = distance_squared_test > 4
y_test = torch.zeros_like(distance_squared_test, dtype=torch.long)
y_test[mask_one_test] = 1
y_test[mask_two_test] = 2

# Evaluate test data

model_a_test_data = evaluate_model(model_a, x_test, y_test)

model_b_test_data = evaluate_model(model_b, x_test, y_test)

model_c_test_data = evaluate_model(model_c, x_test, y_test)

# Print results for comparison

models = [model_a_trained, model_b_trained, model_c_trained]
for key in model_a_trained.keys():
    for index, model in enumerate(models):
        letter = chr(index + 65)
        print(f"Model {letter} -- {key}: {model[key]}")

evaluation_train_data = [model_a_train_data, model_b_train_data, model_c_train_data]
for key in model_a_train_data.keys():
    for index, model in enumerate(evaluation_train_data):
        letter = chr(index + 65)
        print(f"Model {letter} Training -- {key}: {model[key]}")


evaluation_test_data = [model_a_test_data, model_b_test_data, model_c_test_data]
for key in model_a_test_data.keys():
    for index, model in enumerate(evaluation_test_data):
        letter = chr(index + 65)
        print(f"Model {letter} Testing -- {key}: {model[key]}")