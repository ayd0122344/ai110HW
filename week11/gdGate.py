#【mynote】用梯度下降法實現單層感知器
import numpy as np
import math
import gd3 as gd

def sig(t): #【mynote】sigmoid函數，圖形會有梯度消失的問題，所以現在都用relu，只要大於都會有梯度
    return 1.0/(1.0+math.exp(-t))

o = [0,0,0,1] # and gate outputs
'''
output
2999:p=[ 1.70833465  1.70833465 -2.7326384 ] f(p)=0.506 gp=[-0.04493286 -0.04493286  0.06420767] glen=0.09034
o0=0.061 o1=0.264 o2=0.264 o3=0.665 【mynote】用sigmoid的話，<0.5就算是0，>0.5就算是1，結果是0 0 0 1沒問題
'''
# o = [0,1,1,1] # or gate outputs
# o = [0,1,1,0] # xor gate outputs #【mynote】單層感知器做不出xor，因為xor的positive跟negative不是線性可分割
def loss(p, dump=False):
    [w1,w2,b] = p
    o0 = sig(w1*0+w2*0+b)
    o1 = sig(w1*0+w2*1+b)
    o2 = sig(w1*1+w2*0+b)
    o3 = sig(w1*1+w2*1+b)
    delta = np.array([o0-o[0], o1-o[1], o2-o[2], o3-o[3]])
    if dump:
        print('o0={:.3f} o1={:.3f} o2={:.3f} o3={:.3f}'.format(o0,o1,o2,o3))
    return np.linalg.norm(delta, 2)

p = [0.0, 0.0, 0.0] # [w1,w2,b] 
plearn = gd.gradientDescendent(loss, p, max_loops=3000)
loss(plearn, True)
