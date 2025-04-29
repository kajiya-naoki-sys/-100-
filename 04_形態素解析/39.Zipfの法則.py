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
rank = [i + 1 for i in range(0, len(wordCount))]


#!大量のテキストに使用された語句の頻出順位と頻度を集計すると、頻出順位がk番目の頻度は頻出順位1番目の頻度を1/kした値になる法則をジップの法則（ゼータ分布）という。
plt.plot(rank, count)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('ranking', fontsize = 18)
plt.ylabel('count', fontsize = 18)
plt.grid(which='both')

plt.show()