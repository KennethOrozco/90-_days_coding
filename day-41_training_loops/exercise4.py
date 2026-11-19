import torch

x = torch.tensor([1., 2., 3., 4., 5.])
y = torch.tensor([3., 5., 7., 9., 11.])

w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)

learning_rate = 0.01
epochs = 200

# Create an optimizer for w and b

optimizer = torch.optim.SGD(
    [w, b],
    lr=learning_rate
)
# Training loop
for epoch in range(epochs):
    #Clear previous gradients
    optimizer.zero_grad()
    # Forward pass that produceds predictions for all five samples
    predictions = w * x + b
    # MSE loss
    loss = torch.mean((predictions -y) ** 2)
    # Backward pass
    loss.backward()
    #Update parameters
    optimizer.step()
    #Loss log every 20 epoch
    if (epoch +1) % 20 == 0:
        print("Epoch: ", epoch + 1)
        print("Loss: ", loss)

print("Final Weight: ", w)
print("Final Bias: ", b)