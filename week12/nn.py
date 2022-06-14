import random
from micrograd.engine import Value

class Module:

    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0

    def parameters(self):
        return []

class Neuron(Module): #【mynote】一個神經元是一個module

    def __init__(self, nin, nonlin=True):
        self.w = [Value(random.uniform(-1,1)) for _ in range(nin)]
        self.b = Value(0)
        self.nonlin = nonlin

    def __call__(self, x): #【mynote】做正向
        act = sum((wi*xi for wi,xi in zip(self.w, x)), self.b) #【mynote】對每一個w和x都做w*x後加總，最後再跟b加起來
        return act.relu() if self.nonlin else act #【mynote】接著對結果做relu (act.relu())，就是一個神經元的輸出值

    def parameters(self):
        return self.w + [self.b] #【mynote】self.w是一個陣列，python陣列相加就是and

    def __repr__(self):
        return f"{'ReLU' if self.nonlin else 'Linear'}Neuron({len(self.w)})"

class Layer(Module):

    def __init__(self, nin, nout, **kwargs): #【mynote】nin，n個輸入，nout，n個輸出
        self.neurons = [Neuron(nin, **kwargs) for _ in range(nout)]

    def __call__(self, x):
        out = [n(x) for n in self.neurons]
        return out[0] if len(out) == 1 else out

    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()] #【mynote】蒐集所有神經元的參數

    def __repr__(self):
        return f"Layer of [{', '.join(str(n) for n in self.neurons)}]"

class MLP(Module):

    def __init__(self, nin, nouts): #【mynote】demo.py中的2是nin，代表2 layers，[16,16,1]是nouts，代表第一層及第二層各16個神經元，第三層1個神經元
        sz = [nin] + nouts #【mynote】每一層的大小
        self.layers = [Layer(sz[i], sz[i+1], nonlin=i!=len(nouts)-1) for i in range(len(nouts))]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x) #【mynote】一層層代入x
        return x #【mynote】總輸出

    def parameters(self): #【mynote】parameters()將所有w集合成陣列
        return [p for layer in self.layers for p in layer.parameters()]

    def __repr__(self):#【mynote】印出來
        return f"MLP of [{', '.join(str(layer) for layer in self.layers)}]"
