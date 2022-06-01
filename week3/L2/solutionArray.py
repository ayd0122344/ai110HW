from solution import Solution
from random import random, randint

class SolutionArray(Solution):    #【mynote】SolutionArray繼承Solution，括弧並非函數的意思!
    def neighbor(self):           #  多變數解答的鄰居函數。
        nv = self.v.copy()        #  nv=v.clone()=目前解答的複製品
        i = randint(0, len(nv)-1) #  隨機選取一個變數 #【mynote】len(nv)取維度為3，randint(0, len(nv)-1) 在0~3之間隨機取整數，也就是可能取到0或1或2
        if (random() > 0.5):      #  擲骰子決定要往左或往右移
            nv[i] += self.step
        else:
            nv[i] -= self.step
        return SolutionArray(nv)  #  傳回新建的鄰居解答。

    def energy(self): #  能量函數
        x, y, z =self.v #【mynote】(1)四個變數就把x, y, z改成x, y, z, w，以此類推
        return x*x+3*y*y+z*z-4*x-3*y-5*z+8 #  (x^2+3y^2+z^2-4x-3y-5z+8)  #【mynote】(2)改成變數數量後，記得改這行目標方程式

    def str(self):    #  將解答轉為字串的函數，以供列印用。
        return "energy({:s})={:f}".format(str(self.v), self.energy())


