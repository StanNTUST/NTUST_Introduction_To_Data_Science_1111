# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 00:18:36 2022

@author: B11130038 王家宏
"""
import random
number=random.randint(1,100)
guess=int(input("請猜數字1-100："))
while guess!=number:
    if guess>number:
        print("太大了！")
    if guess<number:
        print("太小了！")
    guess=int(input("請猜數字1-100："))
print("猜對了！")