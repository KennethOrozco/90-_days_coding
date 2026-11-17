import torch

def train_weight(
    x: torch.Tensor,
    y: torch.Tensor,
    w: torch.Tensor,
    learning_rate: float,
    epochs: int
) -> torch.Tensor:
    for epoch in range(epochs):
        prediction = x * w
        loss = (prediction - y) ** 2
        loss.backward()
        with torch.no_grad():
            w -= learning_rate * w.grad
        print("Loss: ", loss)    
        w.grad = None
        print("Epoch: ", epoch + 1)
        print("Weight: ", w)
   
    return w

x = torch.tensor(2.0)
y = torch.tensor(8.0)

w = torch.tensor(1.0, requires_grad=True)

learning_rate = 0.1
epochs = 10

print("W: ", train_weight(x, y, w, learning_rate, epochs))