def gradient_step(x:float, y:float, w: float, learning_rate: float):
    prediction = x * w
    og_loss = (prediction - y) ** 2
    gradient = 2 * (prediction - y) * x
    new_w = w - learning_rate * gradient
    new_prediction = x * new_w
    new_loss = (new_prediction - y) ** 2
    return new_w, og_loss, new_loss



x = 2.0
y = 8.0
w = 1.0
learning_rate = 0.1

# Test 1: Negative gradient
print(gradient_step(2.0, 8.0, 1.0, 0.1))

# Test 2: Positive gradient
print(gradient_step(2.0, 2.0, 3.0, 0.1))

new_w, og_loss, new_loss = gradient_step(x, y, w, learning_rate)

print(new_w)
print(og_loss)
print(new_loss)