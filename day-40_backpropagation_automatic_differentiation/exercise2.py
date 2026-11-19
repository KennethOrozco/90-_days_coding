import torch

w = torch.tensor(2.0, requires_grad=True)

a = 2 * w + 1
z = 3 * a
loss = z ** 2

loss.backward()

print(loss)
print(w.grad.item())