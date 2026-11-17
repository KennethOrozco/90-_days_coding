import torch

def compare_activations(values: torch.Tensor) -> None:
    relu = torch.relu(values)
    sigmoid = torch.sigmoid(values)
    tanh = torch.tanh(values)
    print("relu: ", relu)
    print("sigmoid: ", sigmoid)
    print("tanh: ", tanh)

values = torch.tensor([-3.0, -1.0, 0.0, 1.0, 3.0])

compare_activations(values)
