# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 00:17:46 2022

@author: B11130038 王家宏
"""
number=int(input("請輸入1 ~ 100的正整數："))
total=1
for i in range(1,number+1):
    total*=i
print(number,"階乘為",total,sep="")