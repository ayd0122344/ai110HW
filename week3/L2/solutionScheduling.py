#【mynote】非連續函數問題，只要定得出鄰居、高度即可找到解
from random import random, randint, choice
from solution import Solution
import numpy as np

courses = [
{'teacher': '  ', 'name':'　　', 'hours': -1},
{'teacher': '甲', 'name':'機率', 'hours': 2},
{'teacher': '甲', 'name':'線代', 'hours': 3},
{'teacher': '甲', 'name':'離散', 'hours': 3},
{'teacher': '乙', 'name':'視窗', 'hours': 3},
{'teacher': '乙', 'name':'科學', 'hours': 3},
{'teacher': '乙', 'name':'系統', 'hours': 3},
{'teacher': '乙', 'name':'計概', 'hours': 3},
{'teacher': '丙', 'name':'軟工', 'hours': 3},
{'teacher': '丙', 'name':'行動', 'hours': 3},
{'teacher': '丙', 'name':'網路', 'hours': 3},
{'teacher': '丁', 'name':'媒體', 'hours': 3},
{'teacher': '丁', 'name':'工數', 'hours': 3},
{'teacher': '丁', 'name':'動畫', 'hours': 3},
{'teacher': '丁', 'name':'電子', 'hours': 4},
{'teacher': '丁', 'name':'嵌入', 'hours': 3},
{'teacher': '戊', 'name':'網站', 'hours': 3},
{'teacher': '戊', 'name':'網頁', 'hours': 3},
{'teacher': '戊', 'name':'演算', 'hours': 3},
{'teacher': '戊', 'name':'結構', 'hours': 3},
{'teacher': '戊', 'name':'智慧', 'hours': 3}
]

teachers = ['甲', '乙', '丙', '丁', '戊']

rooms = ['A', 'B']

slots = [
'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37',
'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47',
'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57',
'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17',
'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27',
'B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37',
'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47',
'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57',
]

cols = 7

def randSlot() :
    return randint(0, len(slots)-1) #【mynote】回傳隨機取得的slot索引值，如：代表A11的索引值0；代表A12的索引值1...等等

def randCourse() :
    return randint(0, len(courses)-1)#【mynote】回傳隨機取得的courses索引值，如：代表{'teacher': '乙', 'name':'視窗', 'hours': 3}的索引值4


class SolutionScheduling(Solution) :
    def neighbor(self):    # 單變數解答的鄰居函數。
        fills = self.v.copy()
        choose = randint(0, 1) # 【mynote】choose是改變一個or改變兩個的指標，隨機取得0或1
        if choose == 0: # 任選一個改變 
            i = randSlot()#【mynote】回傳隨機取得的slot索引值存在i
            fills[i] = randCourse() # 【mynote】將解答的第i個值(隨機一節課)改成某某課程的索引值，如:將A12(A教室星期一的第二節)改成代表{'teacher': '乙', 'name':'視窗', 'hours': 3}的索引值4
        elif choose == 1: # 任選兩個交換
            i = randSlot() #【mynote】隨機取得的slot索引值存在i
            j = randSlot() #【mynote】隨機取得的slot索引值存在j
            t = fills[i] #【mynote】解答的第i個值存在t
            fills[i] = fills[j]#【mynote】解答的第i個值變成解答的第j個值
            fills[j] = t#【mynote】解答的第j個值變成解答的第i個值
        return SolutionScheduling(fills)                  # 建立新解答並傳回。

    def height(self) :      # 高度函數
        courseCounts = [0] * len(courses)
        fills = self.v
        score = 0
        # courseCounts.fill(0, 0, courses.length)
        for si in range(len(slots)):
            courseCounts[fills[si]] += 1
            #                        連續上課:好                   隔天:不好     跨越中午:不好
            if si < len(slots)-1 and fills[si] == fills[si+1] and si%7 != 6 and si%7 != 3:
                score += 0.1
            if si % 7 == 0 and fills[si] != 0: # 早上 8:00: 不好
                score -= 0.12
        
        for ci in range(len(courses)):
            if (courses[ci]['hours'] >= 0):
                score -= abs(courseCounts[ci] - courses[ci]['hours']) # 課程總時數不對: 不好
        return score

    def str(self) :    # 將解答轉為字串，以供印出觀察。
        outs = []
        fills = self.v
        for i in range(len(slots)):
            c = courses[fills[i]]
            if i%7 == 0:
                outs.append('\n') #【mynote】七堂課就換行
            outs.append(slots[i] + ':' + c['name'])
        return 'height={:f} {:s}\n\n'.format(self.height(), ' '.join(outs))
    
    @classmethod #【mynote】基本上class 裡面的function 的第一個參數都需要指向自己，但classmethod綁定的對象也是類別，因此不需要實際建立物件即可呼叫。
    def init(cls):
        fills = [0] * len(slots) #【mynote】[0]表示元素一list只包含一个0。乘以len(slots)可以得到len(slots)個零
        for i in range(len(slots)): #【mynote】1. 先隨機排一組解答fills
            fills[i] = randCourse()
        return SolutionScheduling(fills)#【mynote】2. 讓SolutionScheduling繼承fills，執行鄰居函數&高度函數