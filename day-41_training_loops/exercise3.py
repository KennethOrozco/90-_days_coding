import torch

x = torch.tensor(2.0)
y = torch.tensor(10.0)

w1 = torch.tensor(2.0, requires_grad=True)
b1 = torch.tensor(1.0, requires_grad=True)

w2 = torch.tensor(3.0, requires_grad=True)
b2 = torch.tensor(2.0, requires_grad=True)

learning_rate = 0.001
epochs = 20
optimizer = torch.optim.SGD(
    [w1, b1, w2, b2],
    lr=learning_rate
)
# Training loop
for epoch in range(epochs):
    # Clear previous gradients
    optimizer.zero_grad()
    # Forward pass
    h = w1 * x + b1
    z = w2 * h + b2
    # Calculate loss
    loss = (z -y)**2
    # Backward pass
    loss.backward() 
    # Update parameters
    optimizer.step()
    # Print progress
    print("Epoch: ", epoch + 1)
    print("Loss: ", loss)