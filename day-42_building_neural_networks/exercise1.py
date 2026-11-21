import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

model = SimpleModel()

x = torch.tensor([
    [1.],
    [2.],
    [3.],
    [4.],
    [5.]
])

prediction = model(x)

print(prediction)

for name, parameter in model.named_parameters():
    print(name, parameter)