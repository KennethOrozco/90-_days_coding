import torch

x = torch.tensor(2.0)
y = torch.tensor(10.0)

w1 = torch.tensor(2.0, requires_grad=True)
b1 = torch.tensor(1.0, requires_grad=True)

w2 = torch.tensor(3.0, requires_grad=True)
b2 = torch.tensor(2.0, requires_grad=True)

learning_rate = 0.001

# Perform the forward pass

h = w1 * x + b1

z = w2 * h + b2
# Calculate the loss

loss = (z -y)**2
loss.backward()

print("Og w1: ", w1)
print("Og w2: ", w2)
print("Og b1: ", b1)
print("Og b2: ", b2)

# Update all four parameters using gradient descent

with torch.no_grad():
    w1 -= learning_rate * w1.grad
    w2 -= learning_rate * w2.grad
    b1 -= learning_rate * b1.grad
    b2 -= learning_rate * b2.grad

print("Updated w1: ", w1)
print("Updated w2: ", w2)
print("Updated b1: ", b1)
print("Updated b2: ", b2)
