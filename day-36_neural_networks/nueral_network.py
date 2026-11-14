# Function to get the relu 
def relu(z: float | int) -> float | int:
    if not isinstance(z, (int, float)):
        raise TypeError("Need a number!")
    if z > 0.0:
        return z
    return 0.0

# Calcuate a nueron's acivated output
def neuron(inputs:list[float], weights: list[float], bias: float) -> float:
    if len(inputs) != len(weights):
        raise ValueError("Must have the same number of inputs to weights")
    total = 0
    for index , x in enumerate(inputs):
        total += x * weights[index]
    total += bias
    return relu(total)
        

    


inputs = [2, 3]

hidden1_weights = [0.5, 1]
hidden1_bias = -1

hidden2_weights = [-1, 0.5]
hidden2_bias = 2

output_weights = [2, -1]
output_bias = 0.5
# Use function to find h1 and h2
h1 = neuron(inputs, hidden1_weights, hidden1_bias)

print(h1)

h2 = neuron(inputs, hidden2_weights, hidden2_bias)

print(h2)

# Pass the outputs for the final nueron
h_inputs = [h1, h2]
final_prediction = neuron(h_inputs, output_weights, output_bias)

print(final_prediction)
