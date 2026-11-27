import torch
from torch.utils.data import TensorDataset

x = torch.tensor([
    [1.0, 2.0],
    [3.0, 4.0],
    [5.0, 6.0],
    [7.0, 8.0],
    [9.0, 10.0],
    [11.0, 12.0]
])

y = torch.tensor([0, 1, 2, 0, 1, 2])
# Create dataset
dataset = TensorDataset(x,y)
# Print total number of samples
print("Number of samples", len(dataset))
# Print first sample and its corresponding label
first_sample, first_label = dataset[0]
print(f"First Sample: {first_sample} -- Label: {first_label}")
# Print the last sample and its corresponding label
last_sample, last_label = dataset[-1]
print(f"Last Sample: {last_sample} -- Label: {last_label}")
# Retrieve sample at index 2 and unpack to separate labels
sample_at_2, label_at_2 = dataset[2]
# Print shape of unpacked variables
print("Sample Shape: ", sample_at_2.shape)
print("Label Shape: ", label_at_2.shape)
print("Sample Data Type: ", sample_at_2.dtype)
print("Label Data Type: ", label_at_2.dtype)
# Use a for loop print each sample and corresponding label
# Count samples per class
class_names = ("class_zero", "class_one", "class_two")
samples_per_class = {name: 0 for name in class_names}

for index, (sample, label) in enumerate(dataset, start=1):
    print(f"Sample #{index}: {sample} -- Label: {label}")
    samples_per_class[class_names[label]] += 1


print(samples_per_class)
    



