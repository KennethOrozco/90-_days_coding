import torch

x = torch.tensor(2.0)
y = torch.tensor(10.0)

w1 = torch.tensor(2.0, requires_grad=True)
b1 = torch.tensor(1.0, requires_grad=True)

w2 = torch.tensor(3.0, requires_grad=True)
b2 = torch.tensor(2.0, requires_grad=True)

h = w1 * x + b1
z = w2 * h + b2
loss = (z - y)**2
loss.backward()

print(w1.grad.item())
print(b1.grad.item())

print(w2.grad.item())
print(b2.grad.item())