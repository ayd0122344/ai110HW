step = 0.01

# 我們想找函數 f 的最低點
def f(p):
    [x,y] = p #【mynote】p是一個二維的數，有兩個變數(x跟y)
    return x * x + y * y

# df(f, p, k) 為函數 f 對變數 k 的偏微分: df / dp[k]
# 例如在上述 f 範例中 k=0, df/dx, k=1, df/dy
def df(f, p, k): #【mynote】f在p點對第k軸的偏微分，第0軸就是對x軸的偏微分，第1軸就是對y軸的偏微分
    p1 = p.copy()
    p1[k] += step
    return (f(p1) - f(p)) / step

# 函數 f 在點 p 上的梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)): #【mynote】對p點的每一個軸
        gp[k] = df(f, p, k) #【mynote】都進行偏微分
    return gp

[x,y] = [1,3]
print('x=', x, 'y=', y)
print('df(f(x,y), 0) = ', df(f, [x, y], 0)) #【mynote】計算f對[x,y]這一點第0軸的偏微分，這裡output:2
print('df(f(x,y), 1) = ', df(f, [x, y], 1)) #【mynote】計算f對[x,y]這一點第1軸的偏微分，這裡output:6
print('grad(f)=', grad(f, [x,y]))  #【mynote】將第0軸與第1軸偏微分的結果合起來就是梯度，這裡output:[2,6]

#【mynote】npGradient.py是用numpy寫的版本，numpy在高維的時候會方便很多，因為numpy有支援向量的+-*/，甚至矩陣的計算。
#【mynote】numpy最重要的功能就是有支援高維的矩陣，所謂的張量其實就是高維的矩陣。