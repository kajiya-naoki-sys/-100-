import collections
from matplotlib import pyplot as plt
import japanize_matplotlib

link = '/workspace/04_形態素解析/neko.txt.mecab'
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
word, count = zip(*wordCount.most_common())
plt.hist(count, bins=50)
plt.show()