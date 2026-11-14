import torch

# Function that uses Pytorch built in operations to find the relu
def neuron(inputs: torch.tensor, weights: torch.tensor, bias: float) -> torch.tensor:
    z = torch.dot(inputs, weights) + bias
    return torch.relu(z)

inputs = torch.tensor([2.0, 3.0])
weights = torch.tensor([0.5, 1.0])
bias = -1.0

print(neuron(inputs, weights, bias))