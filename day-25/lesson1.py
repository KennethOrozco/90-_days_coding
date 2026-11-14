import math

inputs = [2, 0, -2]

for z in inputs:
    sigma = 1 / (1 + math.exp(-z))
    print(sigma)
    if sigma >= 0.5:
        classification = 1
    else: 
        classification = 0

    print(classification)

