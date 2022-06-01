import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([2, 3, 4, 5, 6], dtype=np.float32)
# x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
# y = np.array([1.9, 3.1, 3.9, 5.0, 6.2], dtype=np.float32)

def predict(a, xt):
	return a[0]+a[1]*xt

def MSE(a, x, y):
	total = 0
	for i in range(len(x)):
		total += (y[i]-predict(a,x[i]))**2
	return total

def loss(p):
	return MSE(p, x, y)
def optimize():
    # 請修改這個函數，自動找出讓 loss 最小的 p
    p = [0.0,0.0]
    t_loss = loss(p)
    failCount = 0 
    while (failCount < 30000):
        p[0]=p[0] + 0.01
        p[1]=p[1] + 0.01
        if loss(p) < t_loss:
            t_loss = loss(p)
        else:
            p[0]=p[0] - 0.01
            p[1]=p[1] - 0.01
            failCount = failCount + 1
        p[0]=p[0] - 0.01
        p[1]=p[1] - 0.01
        if loss(p) < t_loss:
            t_loss = loss(p)
        else:
            p[0]=p[0] + 0.01
            p[1]=p[1] + 0.01
            failCount = failCount + 1
        p[0]=p[0] + 0.01
        p[1]=p[1] - 0.01
        if loss(p) < t_loss:
            t_loss = loss(p)
        else:
            p[0]=p[0] - 0.01
            p[1]=p[1] + 0.01
            failCount = failCount + 1
        p[0]=p[0] - 0.01
        p[1]=p[1] + 0.01
        if loss(p) < t_loss:
            t_loss = loss(p)
        else:
            p[0]=p[0] + 0.01
            p[1]=p[1] - 0.01
            failCount = failCount + 1
    return p

p = optimize()

# Plot the graph
y_predicted = list(map(lambda t: p[0]+p[1]*t, x))
print('y_predicted=', y_predicted)
plt.plot(x, y, 'ro', label='Original data')
plt.plot(x, y_predicted, label='Fitted line')
plt.legend()
plt.show()

# 執行結果 100%原創
# [1.9700000000000015, 1.0100000000000007]
# y_predicted= [1.9700000000000015, 2.980000000000002, 3.990000000000003, 5.0000000000000036, 6.010000000000004]