import torch

# Make one dimensional tensor
one_dimensional = torch.tensor([10, 20, 30, 40])
# Make a two dimension tensor
two_dimensional = torch.tensor([
    [34, 22, 54],
    [89, 92, 32]
])

#Print the shape and number of dimensions for both
print(one_dimensional.shape)
print(one_dimensional.ndim)

print(two_dimensional.shape)
print(two_dimensional.ndim)

#Create two tensor, and print their element-wise sum and product

x = torch.tensor([1, 2, 3])

y = torch.tensor([4, 5, 6])

print(x)
print(y)
print(x + y)

