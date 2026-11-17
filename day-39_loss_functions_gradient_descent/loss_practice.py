import torch
def mean_squared_error(actual: torch.Tensor, predicted: torch.Tensor) -> torch.Tensor:
    if len(actual) != len(predicted):
        raise ValueError("Number of values in actual and predicted are not the same!")
    return torch.mean((actual - predicted) ** 2)

actual = torch.tensor([3.0, 5.0, 2.0])
predicted = torch.tensor([2.0, 7.0, 4.0])

print(mean_squared_error(actual, predicted))