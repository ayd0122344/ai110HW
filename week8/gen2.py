import random as r

'''
S = NP VP
NP = DET N
VP = V NP
N = dog | cat
V = chase | eat
DET = a | the
'''

def S(p):
    p['p'] = 1.0
    return NP(p) + VP(p)

def NP(p):
    return DET(p) + N(p)

def VP(p):
    return V(p) + NP(p)

def choose(words, probs):
    i = r.randrange(len(words))
    return (words[i], probs[i])

def genWords(words, probs, p):
    word, prob = choose(words, probs)
    p['p'] = p['p'] * prob
    return [word]

def N(p):
    return genWords(['dog', 'cat'], [0.3, 0.7], p) #【mynote】加上產生的機率

def V(p):
    return genWords(['chase', 'eat'], [0.6, 0.4], p)

def DET(p):
    return genWords(['a', 'the'], [0.5, 0.5], p)

p = {'p': 1.0}

for _ in range(10):
    print('%s %f'%(S(p), p['p']))


#【mynote】output如下，將每一種可能產生的結果之機率算出
'''
['a', 'cat', 'chase', 'a', 'cat'] 0.073500
['a', 'dog', 'eat', 'a', 'dog'] 0.009000      
['the', 'cat', 'eat', 'a', 'dog'] 0.021000    
['a', 'cat', 'chase', 'a', 'cat'] 0.073500    
['the', 'cat', 'chase', 'the', 'dog'] 0.031500
['the', 'dog', 'chase', 'the', 'dog'] 0.013500
['the', 'cat', 'chase', 'the', 'cat'] 0.073500
['the', 'dog', 'eat', 'a', 'dog'] 0.009000
['a', 'dog', 'eat', 'the', 'cat'] 0.021000
['a', 'cat', 'chase', 'the', 'dog'] 0.031500
'''