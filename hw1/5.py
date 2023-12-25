# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 00:18:59 2022

@author: B11130038 王家宏
"""
def salary(hours,hourlypay,bonus):
    return hours*hourlypay+bonus

hours=80
hourlypay=170
bonus=0
print("工作時數%d、時薪%d、沒有獎金的薪資為%d"%(hours,hourlypay,salary(hours,hourlypay,bonus)))
hours=int(input("請輸入工作時數："))
hourlypay=int(input("請輸入時薪："))
bonus=int(input("請輸入獎金："))
print("工作時數%d、時薪%d、獎金%d的薪資為%d"%(hours,hourlypay,bonus,salary(hours,hourlypay,bonus)))