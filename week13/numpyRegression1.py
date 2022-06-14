import numpy as np
import math

# Create random input and output data
x = np.linspace(-math.pi, math.pi, 2000)  #【mynote】x的大小是2000維。linspace是線性空間，從-pi到+pi平均切成2000個點。
y = 0+1*x+2*x**2+3*x**3 # np.sin(x) #【mynote】y的大小也是2000維

# Randomly initialize weights
a = np.random.randn()
b = np.random.randn()
c = np.random.randn()
d = np.random.randn()

learning_rate = 1e-6
for t in range(2000):
    # Forward pass: compute predicted y
    # y = a + b x + c x^2 + d x^3
    y_pred = a + b * x + c * x ** 2 + d * x ** 3 #【mynote】3次回歸的曲線 #【mynote】y_pred的大小也是2000維

    # Compute and print loss
    loss = np.square(y_pred - y).sum() #【mynote】正向計算將loss算出來 #【mynote】2000個loss加總
    if t % 100 == 99:
        print(t, loss)

    # Backprop to compute gradients of a, b, c, d with respect to loss
    grad_y_pred = 2.0 * (y_pred - y) #【mynote】最後的loss就是最後那層的預設梯度 #【mynote】推導過程請見「numpyRegression1之a的梯度推導.jpg」，(y_pred - y)趨近於a的值
    #【mynote】算出a,b,c,d的梯度
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x).sum()
    grad_c = (grad_y_pred * x ** 2).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    # Update weights    #【mynote】對a,b,c,d作微調，往梯度的方向走，算出最佳的a,b,c,d值
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d

print(f'Result: y = {a} + {b} x + {c} x^2 + {d} x^3')