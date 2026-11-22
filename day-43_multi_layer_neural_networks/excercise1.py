import torch
import torch.nn as nn

class MultiLayerModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.linear1 = nn.Linear(2, 4)
        self.linear2 = nn.Linear(4, 3)
        self.linear3 = nn.Linear(3, 1)

    def forward(self, x):
        x = self.linear1(x)
        print(f"layer1 shape: {x.shape}")
        x = self.linear2(x)
        print(f"layer2 shape: {x.shape}")
        x = self.linear3(x)
        print(f"layer3 shape: {x.shape}")
        return x

model = MultiLayerModel()

x = torch.tensor([
    [3., 2.],
    [5., 3.],
    [6., 5.],
    [2., 2.],
    [6., 3.]
])

prediction = model(x)

print(prediction)

for name, parameter in model.named_parameters():
    print(name, parameter.shape)



