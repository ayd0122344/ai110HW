#【mynote】torchGd1是當作沒有pytorch可以用寫出來的，torchGd2容許傳入多變數函數
#【mynote】torchGd3就使用pytorch的forward、backward，並把取出來的梯度乘-1後加回去(梯度下降法)
import torch
import math

dtype = torch.float
x = torch.randn((), dtype=dtype, requires_grad=True) # torch.linspace(-math.pi, math.pi, 2000)

def loss_fn(x):
	loss = x*x-4*x+4 #【mynote】(x-2)^2展開，最低點(x)應該要是2，loss應該要是0
	return loss

def GD(x, loss_fn, loop_max = 10000, learning_rate = 1e-3):
	for t in range(loop_max):
		loss = loss_fn(x) #【mynote】loss funciton
		if t % 100 == 99:
			print(t, 'x=', x.item(), 'loss=', loss.item())
		loss.backward()
		with torch.no_grad():
			x -= learning_rate * x.grad #【mynote】算出x梯度，learning_rate = 1e-3，10的-3次方
			x.grad = None

GD(x, loss_fn, loop_max = 5000)

print(f'Result: x = {x.item()} loss={loss_fn(x)}')