from os import path
from persian_wordcloud.wordcloud import PersianWordCloud, add_stop_words
from wordcloud import STOPWORDS as EN_STOPWORDS
from wordcloud import wordcloud, STOPWORDS, WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
import os

workbook = xlrd.open_workbook("data/2-p9vcb5bb.xlsx")
sheet = workbook.sheet_by_index(0)
plt.rcParams.update({'font.family' : 'Arial'})


comment = [str(cell.value) for cell in sheet.col(9)]

comment_word=[]
stopwords = set(STOPWORDS)


varrr = ''
for i in range(1, len(comment)):
    varrr = comment[i].split()

    for j in range(varrr.__len__()):
        comment_word.append(varrr[j])

ll = ''
p = int(comment_word.__len__() / 100)
for k in range(p):
    ll = ll + comment_word[k] + ' '


wordcloud =\
        PersianWordCloud(
            only_persian=True,
            max_words=100000,
            width = 800,
            height=800,
            background_color='white',
            stopwords=stopwords,
            min_font_size=10).generate(ll)


plt.figure(figsize=(8, 8), facecolor= None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
plt.savefig('word_cloud.png')
WordCloud.to_file(os.path.join('/data', 'wc.png'))
