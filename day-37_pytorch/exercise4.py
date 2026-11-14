import torch

#Calculate the weighted sum for each neuron, adds each nueron's bias, and applies relu
def layer(inputs: torch.Tensor, weights:torch.Tensor, biases: torch.Tensor) -> torch.Tensor:
    if len(weights) != len(biases):
        raise ValueError("Length of weights and biases are not the same!")
    if len(inputs) != len(weights[0]):
        raise ValueError("number of inputs and and number of weights per nueron are not the same!")
    z = torch.matmul(weights, inputs) + biases
    return torch.relu(z)
    
        



inputs = torch.tensor([2.0, 3.0])

weights = torch.tensor([
    [0.5, 1.0],
    [1.0, -1.0],
    [-0.5, 2.0]
])

biases = torch.tensor([-1.0, 0.5, -2.0])

result = layer(inputs, weights, biases)

print(result)