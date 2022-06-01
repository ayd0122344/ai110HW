import random
# 【mynote】本程式無法通用於高維度，因為變數多一個就得多加一個elif，當有10個變數就要寫1024條。
def hillClimbing(f, x, y, h=0.01): # 【mynote】h為步伐
    while (True):
        fxy = f(x, y) # 【mynote】取目前的點的值
        print('x={0:.3f} y={1:.3f} f(x,y)={2:.3f}'.format(x, y, fxy))
        if f(x+h, y) >= fxy: # 【mynote】x加一點點看有沒有比目前的點更好
            x = x + h
        elif f(x-h, y) >= fxy:# 【mynote】x減一點點看有沒有比目前的點更好
            x = x - h
        elif f(x, y+h) >= fxy:# 【mynote】y加一點點看有沒有比目前的點更好
            y = y + h
        elif f(x, y-h) >= fxy:# 【mynote】y減一點點看有沒有比目前的點更好
            y = y - h
        else:
            break # 都沒有更好代表目前的點是最佳解
    return (x,y,fxy)

def f(x, y):
    return -1 * ( x*x - 2*x + y*y + 2*y - 8 )

hillClimbing(f, 0, 0)