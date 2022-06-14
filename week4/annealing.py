# 當溫度很高的時候，模擬退火法基本上就像隨機亂走一樣，
# 但是當溫度逐漸下降之後，模擬退火法就會逐漸凝固，只能朝著較好的解前進，向著較差解前進的機率會逐漸縮小。
# 當溫度幾乎降到零的時候，模擬退火法基本上就會退化成爬山演算法，於是最後還是會固定在某個「區域最佳解」上面。
# 但是由於經過從高溫緩慢降溫的過程，所以模擬退火法比較有機會在高溫時跳出區域最佳解，然後找到更好的解，甚至是全域最佳解之後才凝固。
import math
import random

def P(e, enew, T): # 模擬退火法的機率函數
    if (enew < e):
        return 1
    else:
        return math.exp((e-enew)/T) #【mynote】T是目前的溫度。新的能量跟舊的能量之間我們計算一個機率，如果這個機率比我們取得的亂數大，我們就移動過去。

def annealing(s, maxGens) : # 模擬退火法的主要函數
    sbest = s                              # sbest:到目前為止的最佳解
    ebest = s.energy()                     # ebest:到目前為止的最低能量
    T = 100                                # 從 100 度開始降溫
    for gens in range(maxGens):            # 迴圈，最多作 maxGens 這麼多代。
        snew = s.neighbor()                # 取得鄰居解
        e    = s.energy()                  # e    : 目前解的能量
        enew = snew.energy()               # enew : 鄰居解的能量
        T  = T * 0.995                     # 每次降低一些溫度
        #【mynote】random.random()產生的亂數範圍介於0到1之間，所以當(e-enew)/T趨近於0，math.exp((e-enew)/T)等於1的情況下，不管結果如何都會移過去
        #【mynote】energy越小越好，若enew變高，e-enew是個負數假設為-1，又溫度為初始值1的話，e^-1約0.36，機率很低就不太會移動
        if P(e, enew, T)>random.random():  # 根據溫度與能量差擲骰子，若通過 
            s = snew                       # 則移動到新的鄰居解
            print("{} T={:.5f} {}".format(gens, T, s.str())) # 印出觀察

        if enew < ebest:                 # 如果新解的能量比最佳解好，則更新最佳解。
            sbest = snew
            ebest = enew
    
    print("solution: {}", sbest.str())     # 印出最佳解
    return sbest                           # 傳回最佳解
