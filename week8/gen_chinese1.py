import random as r

#【mynote】S產生NP+VP，NP產生DET+N，VP產生V+NP，N產生狗或貓，V產生追或吃，DET產生一隻或這隻
#【mynote】NP:名詞子句，VP:動詞子句，DET:定詞，N:名詞
#【mynote】屬於context-free，與上下文無關的語句
'''
S = NP VP
NP = DET N
VP = V NP
N = 狗 | 貓
V = 追 | 吃
DET = 一隻 | 這隻
'''

def S():
    return NP() + ' ' + VP()

def NP():
    return DET() + ' ' + N()

def VP():
    return V() + ' ' + NP()

def N():
    return r.choice(['狗', '貓'])

def V():
    return r.choice(['追', '吃'])

def DET():
    return r.choice(['一隻', '這隻'])

print(S())
