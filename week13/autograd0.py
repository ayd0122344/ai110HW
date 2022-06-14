#【mynote】pytorch有內建自動微分的功能，效能比micrograd好很多
#【mynote】本程式使用pytorch的tensor，autograd1.py使用pytorch的ones
import torch 
'''
x = net.variable(1)
y = net.variable(3)
x2 = net.mul(x, x)
y2 = net.mul(y, y)
o  = net.add(x2, y2)

print('net.forward()=', net.forward())
print('net.backwward()')
net.backward()
'''
x = torch.tensor(1., requires_grad=True) #【mynote】建立一個tensor(張量)為1，requires_grad設為True就會有梯度
y = torch.tensor(3., requires_grad=True)
#【mynote】目前x跟y這兩個張量(任意維度的矩陣)都還是純量(單純一個數字)
x2 = x*x
y2 = y*y
o = x2+y2 #【mynote】x^2+y^2

o.backward()

print(x.grad)    # x.grad = 2 
print(y.grad)    # y.grad = 6
#【mynote】x是1，y是3，目標函數是x^2+y^2，對x取梯度就是2x，對y取梯度就是2y，所以x.grad = 2(2*1)，y.grad = 6(2*3)
print(o)    # o.value = 10 #【mynote】正向計算的結果
print(o.item())