import torch
def predict_probability(
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
       return torch.sigmoid(y)

inputs = torch.tensor([2.0, 1.0])

weights1 = torch.tensor([
    [0.5, 1.0],
    [-1.0, 2.0]
])

biases1 = torch.tensor([0.0, 0.5])

weights2 = torch.tensor([
    [1.0, -0.5]
])

biases2 = torch.tensor([-0.5])

output_tensor = predict_probability(inputs, weights1, biases1, weights2, biases2)

print(output_tensor)