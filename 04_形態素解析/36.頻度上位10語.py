import collections
from matplotlib import pyplot as plt
#matplotlibに日本語を対応させる.
import japanize_matplotlib

link = '/Users/kajiyanaoki/Desktop/python/自然言語処理100本ノック/第4章_形態素解析/neko.txt.mecab'
with open(link) as f:
    text = f.read().split('\n')
result = []
for i in text:
    if i == 'EOS' or i == '':
        continue
    ls = i.split('\t')
    tmp = ls[1].split(',')
    d = {}
    d = {'surface': ls[0], 'base': tmp[6], 'pos': tmp[0], 'pos1': tmp[1]}
    result.append(d)

wordList = []
for i in result:
    if i['pos'] == '記号':
        continue
    wordList.append(i['base'])
wordCount = collections.Counter(wordList)
word, count = zip(*wordCount.most_common()[:10])
print(wordCount.most_common()[:10])
plt.bar(word, count)
plt.show()