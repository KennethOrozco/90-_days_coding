import torch

w = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(2.0, requires_grad=True)

z = 3 * w + b

loss = z**2

loss.backward()

weight_gradient = w.grad

bias_gradient = b.grad

print(loss)
print(weight_gradient.item())
print(bias_gradient.item())