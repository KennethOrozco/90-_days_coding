import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(3, 2)

    def forward(self, x):
        return self.linear(x)

model = SimpleModel()

x = torch.tensor([
    [1., 2., 3.],
    [2., 5., 3.],
    [3., 6., 2.],
    [4., 3., 2.],
])

prediction = model(x)

print(prediction)

print("input shape: ", x.shape)
print("output shape: ", prediction.shape)

for name, parameter in model.named_parameters():
    print(name, parameter.shape)