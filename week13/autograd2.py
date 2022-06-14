import torch
#【mynote】一個變數可以是一個tensor，一個tensor可以是任意維度的張量
x = torch.tensor([1.0,2.0], requires_grad=True) #【mynote】x是長度為2的向量
z = x.norm() #【mynote】向量長度，x^2+y^2後開根號
z.backward()
print('z=', z)
print('x.grad=', x.grad)