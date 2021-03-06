class Node:
    def __init__(self, v = 0, g = 0):
        self.v = v # 輸出值 (f(x))
        self.g = g # 梯度值 (偏微分) #【mynote】每一個物件都有v(value)跟g(gradient)，v是正向算出來的值，g是逆向做反傳遞算出來的值

    def __str__(self):
        return 'v:{self.v} g:{self.g}'.format(self=self)

class Gate:
    def __init__(self, o, x, y, f, gfx, gfy):
        self.o = o
        self.x = x
        self.y = y
        self.f = f
        self.gfx = gfx
        self.gfy = gfy

    def forward(self):
        self.o.v = self.f(self.x.v, self.y.v) #【mynote】forward正向，代正向的值進去函數計算
        return self.o.v

    def backward(self):
        x, y, o, gfx, gfy = self.x, self.y, self.o, self.gfx, self.gfy #【mynote】backward逆向，算偏微分
        x.g += gfx(x.v,y.v) * o.g
        y.g += gfy(x.v,y.v) * o.g

    def adjust(self, step=0.001): # 朝逆梯度的方向走一小步
        x, y = self.x, self.y
        x.v -= step*x.g
        y.v -= step*y.g
        x.g = 0
        y.g = 0

class Net:
    def __init__ (self):
        self.gates = []

    def variable (self, v, g=0):
        return Node(v, g)

    def op (self, x, y, f, gfx, gfy):
        o = Node() #【mynote】每加一個op(operation)就是多加一個閘
        g = Gate(o, x, y, f, gfx, gfy)
        self.gates.append(g)
        self.o = o
        return o

    def add (self, x, y): #【mynote】add運算
        return self.op(x, y, lambda x,y:x+y, lambda x,y:1, lambda x,y:1) #【mynote】加入add閘
    def mul (self, x, y): #【mynote】multiple運算
        return self.op(x, y, lambda x,y:x*y, lambda x,y:y, lambda x,y:x) #【mynote】加入multiple閘

    def forward(self): # 正向傳遞計算結果
        for gate in self.gates:
            gate.forward()
        return self.o.v

    def backward(self): # 反向傳遞計算梯度 
        self.o.g = 1 # 設定輸出節點 o 的梯度為 1
        for gate in reversed(self.gates): # 反向傳遞計算每個節點 Node 的梯度 g
            gate.backward()

    def adjust(self, step=0.01): # 朝逆梯度的方向走一小步
        for gate in self.gates:
            gate.adjust(step)

    # 使用 forward-backward 的方式計算梯度的梯度下降法
    def gradient_descendent (self, maxLoops=100, dumpPeriod=1, step=0.01):
        for loop in range(maxLoops): #【mynote】最多執行maxLoops次
            energy = self.forward() #【mynote】每一次都先做前向的計算
            if loop % dumpPeriod==0:
                print(loop, ' => ', energy)
            self.backward() #【mynote】做逆向計算
            self.adjust(step) #【mynote】走一小步

