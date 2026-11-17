import torch

def compare_gradients(
    x: float,
    y: float,
    w: float,
    learning_rate: float
) -> float:
    x_tensor = torch.tensor(x)
    y_tensor = torch.tensor(y)
    w_tensor = torch.tensor(w, requires_grad=True)
    prediction = x_tensor * w_tensor
    loss = (prediction -  y_tensor) ** 2
    manual_grad = 2 * (prediction - y_tensor) * x
    loss.backward()
    auto_grad = torch.tensor(w_tensor.grad.item())
    print("manual grad: ", manual_grad)
    print("auto grad: ", auto_grad)
    print(torch.isclose(manual_grad, auto_grad))
    return  float(w_tensor - learning_rate * auto_grad)



# Test 1: Negative gradient
print(compare_gradients(2.0, 8.0, 1.0, 0.1))

# Test 2: Positive gradient
print(compare_gradients(2.0, 2.0, 3.0, 0.1))