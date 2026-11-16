import torch

def forward(
    inputs: torch.Tensor,
    weights1: torch.Tensor,
    biases1: torch.Tensor,
    weights2: torch.Tensor,
    biases2: torch.Tensor
) -> torch.Tensor:
       if len(weights1) != len(biases1):
        raise ValueError("Length of weights and biases are not the same!")
       if len(inputs) != len(weights1[0]):
        raise ValueError("number of inputs and and number of weights per nueron are not the same!")
       z1= torch.matmul(weights1, inputs) + biases1
       h = torch.relu(z1)
       if len(weights2) != len(biases2):
        raise ValueError("Length of weights and biases are not the same!")
       if len(h) != len(weights2[0]):
        raise ValueError("number of inputs and and number of weights per nueron are not the same!")
       y = torch.matmul(weights2, h) + biases2
       return torch.relu(y)



inputs = torch.tensor([1.0, 2.0])

# Hidden layer: 2 inputs -> 2 neurons
weights1 = torch.tensor([
    [1.0, 0.5],
    [-1.0, 2.0]
])

biases1 = torch.tensor([0.0, -1.0])

# Output layer: 2 hidden neurons -> 1 neuron
weights2 = torch.tensor([
    [0.5, 1.0]
])

biases2 = torch.tensor([-1.0])

output_tensor = forward(inputs, weights1, biases1, weights2, biases2)

print(output_tensor)