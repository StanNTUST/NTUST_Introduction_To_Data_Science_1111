# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 02:10:00 2022

@author: B11130038 王家宏
"""
import qrcode
path="https://www.wanggahong.com/"
img=qrcode.make(path)
print(type(img))
print(img.size)
img.show()
img.save("mywebsite.png",format="PNG")