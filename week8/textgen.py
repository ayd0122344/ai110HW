#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import random,readJSON

data = readJSON.读JSON文件("data.json")
名人名言 = data["famous"] # a 代表前面垫话，b代表后面垫话
前面垫话 = data["before"] # 在名人名言前面弄点废话
后面垫话 = data['after']  # 在名人名言后面弄点废话
废话 = data['bosh'] # 代表文章主要废话来源
#【mynote】eg."爱迪生a，天才是百分之一的勤奋加百分之九十九的汗水。b"，其中a是前面墊話，b是後面墊話。

xx = "学生会退会"

重复度 = 2

def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度 #【mynote】列表轉成list。list * 重複度代表反覆出現「重複度」次。
    while True:
        random.shuffle(池) #【mynote】shuffle就是洗牌。shuffle() 方法将序列(list)的所有元素随机排序。
        for 元素 in 池:
            yield 元素#【mynote】最後把「元素」丟出來

下一句废话 = 洗牌遍历(废话) #【mynote】废话、名人名言都是「列表」
下一句名人名言 = 洗牌遍历(名人名言)

def 来点名人名言():
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace(  "a",random.choice(前面垫话) )
    xx = xx.replace(  "b",random.choice(后面垫话) )
    return xx

def 另起一段(): #【mynote】加入換行
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx

if __name__ == "__main__":
    xx = input("请输入文章主题:") #【mynote】1.先輸入文章主題
    for x in xx:
        tmp = str() #【mynote】2.不斷地產生句子
        while ( len(tmp) < 6000 ) :
            分支 = random.randint(0,100)
            if 分支 < 5:
                tmp += 另起一段() #【mynote】如果亂數<5，則產生新段落
            elif 分支 < 20 :
                tmp += 来点名人名言() #【mynote】如果亂數<20，則加入名言
            else:
                tmp += next(下一句废话) #【mynote】如果亂數不<20，則加入廢話
        tmp = tmp.replace("x",xx) #【mynote】如果有出現x，就代換成我們輸入的標題
        print(tmp)
