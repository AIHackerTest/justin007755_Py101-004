# -*- coding: utf-8 -*-
import random

ranNum = random.randint(1,20)
print("The game started: ")

for i in range(10):
    yourGuess = int(input("第%d次,请输入您猜的数: " % (i+1))) # 这里可以做的再好一点，防止用户输入非数字
    if yourGuess > ranNum:
        print("你猜的数太大了，小一点！")
    elif yourGuess < ranNum:
        print("你猜的数太小了，大一点！")
    else:
        print("恭喜您，答对了！你总共猜了%d次" % (i+1))
        break
