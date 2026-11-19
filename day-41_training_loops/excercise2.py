import torch

x = torch.tensor(2.0)
y = torch.tensor(10.0)

w1 = torch.tensor(2.0, requires_grad=True)
b1 = torch.tensor(1.0, requires_grad=True)

w2 = torch.tensor(3.0, requires_grad=True)
b2 = torch.tensor(2.0, requires_grad=True)

learning_rate = 0.001
epochs = 20

print("Og w1: ", w1)
print("Og w2: ", w2)
print("Og b1: ", b1)
print("Og b2: ", b2)

# Training loop
for epoch in range(epochs):
    # Clear previous gradients
    w1.grad = None
    w2.grad = None
    b1.grad = None
    b2.grad = None
    # Forward pass
    h = w1 * x + b1
    z = w2 * h + b2
    # Calculate loss
    loss = (z -y)**2
    # Backward pass
    loss.backward() 
    # Update parameters
    with torch.no_grad():
        w1 -= learning_rate * w1.grad
        w2 -= learning_rate * w2.grad
        b1 -= learning_rate * b1.grad
        b2 -= learning_rate * b2.grad
    # Print progress
    print("Epoch: ", epoch + 1)
    print("Loss: ", loss)

