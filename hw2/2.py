# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 02:04:35 2022

@author: B11130038 王家宏
"""
# - * - coding: utf - 8 -*-
import numpy as np
import jieba
import matplotlib.pyplot as plt
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#from collections import Counter

# Get dir path of the text.
dpath = path.dirname(__file__)

# Use numpy to read the mask.
#改成愛心
cloud_image = np.array(Image.open(path.join(dpath, "heart.png")))

# Change to big5 dictionary
#jieba.set_dictionary('dict.txt.big.txt')

# Customize stopwords set.
stopwords = set(STOPWORDS)
stopwords.add("")

# Give attributes to our WordCloud.
#wc = WordCloud(font_path='TaipeiSansTCBeta-Regular.ttf', background_color="white", max_words=200, mask=cloud_image,
#               stopwords=stopwords, max_font_size=40, random_state=42,
#               width=1000, height=860, margin=2)
wc = WordCloud(font_path='TaipeiSansTCBeta-Regular.ttf', background_color="white",
               mask=cloud_image, stopwords=stopwords)

# Extend words list in jieba.
#改成教宗的名字
my_words_list = ['方濟各']

def add_word(list):
    for items in list:
        jieba.add_word(items)

add_word(my_words_list)

# Read the whole text.
#換文件檔案裡的文字
text = open(path.join(dpath, 'ChineseIntro.txt')).read()

def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open('stopwords01.txt', 'r', encoding='ANSI')
    try:
        f_stop_text = f_stop.read( )
    finally:
        f_stop.close( )
    f_stop_seg_list=f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist)

text = jiebaclearText(text)
#diction = Counter(text)

wc.generate(text)
#wc.generate_from_frequencies(frequencies=diction)  #產生文字雲

# create coloring from image
cloud_coloring = ImageColorGenerator(cloud_image)

#show
plt.figure(figsize=(8,8))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()

# recolor show
plt.figure(figsize=(8,8))
plt.imshow(wc.recolor(color_func=cloud_coloring), interpolation="bilinear")
plt.axis("off")
plt.show()

# save to file
#改成愛心
wc.to_file("ChineseWordheart.png")  