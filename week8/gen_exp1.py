#【mynote】隨機產生運算式，再用eval計算出結果
import random as r

#【mynote】E隨機產生一個運算式，N(數字)或是E加減乘除E
#【mynote】三引號可以寫多行文件註釋，也可以定義多行字串
'''
E = N | E [+/-*] E 
N = 0-9
'''

def E():
	gen = r.choice(["N", "EE"])
	# print('gen=', gen)
	if gen == "N":
		return N()
	else:
		return E() + r.choice(["+", "-", "*", "/"]) + E()

def N():
	return r.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

e = E()
print(e, "=", eval(e))


