import torch
from torch.utils.data import TensorDataset, DataLoader

torch.manual_seed(42)

x = torch.arange(1, 21, dtype=torch.float32).reshape(10, 2)

y = torch.tensor([0, 1, 2, 0, 1, 2, 0, 1, 2, 0])

dataset = TensorDataset(x, y)

# Creaate Data loader

loader_a = DataLoader(
    dataset,
    batch_size=4,
    shuffle=False
)

#Print the number of batches

print("Loader A batch count: ", len(loader_a))

# Print each batch's features, labels, and tensor shapes
samples_a = 0
for index, (features, labels) in enumerate(loader_a):
    letter = chr(index + 65)
    print(f"Batch {letter}")
    print(f"Features:\n{features}")
    print(f"Labels:{labels}")
    print(f"Feautures Shape: {features.shape}")
    print(f" Labels Shape: {labels.shape}")
    # Count total samples processed
    samples_a += len(features)

print("Loader A total samples: ", samples_a)

#Create a loader that drops last batch
loader_b = DataLoader(
    dataset,
    batch_size=4,
    drop_last=True
)

# Print the batch size for second loader
print("Loader B batch count: ", len(loader_b))

# print its total samples
samples_b = 0
for batch in loader_b:
    samples_b += len(batch[0])

print("Loader B total samples: ", samples_b)

# Create a shuffled loader

loader_c = DataLoader(
    dataset,
    batch_size=4,
    shuffle=True
)
# Observe how shuffling affects with each epoch
for epoch in range(2):
    print(f"Epoch {epoch +1}")
    for index,(features, labels) in enumerate(loader_c):
        letter = chr(index + 65)
        print(f"Batch {letter}")
        print(f"Features:\n{features}")
        print(f"Labels: {labels}")



