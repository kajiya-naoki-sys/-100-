import collections
from matplotlib import pyplot as plt
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

withCatList = []
#!['pos']が名詞/動詞/形容詞の時における['base']の値をwordListに入れる.(リスト内包表記)
wordList = [i['base'] for i in result if i['pos'] in ['名詞', '動詞', '形容詞']]
#!もしwordListに猫が含まれた時.
if '猫' in wordList:
    #?[not in]で含まれないときTrueを返す.猫関連語なのでjが「猫」単体の時や「*」の時は取り除く.
    wordList = [j for j in wordList if j not in ['猫', '*']]
    #wordListとwithCatListはどちらもリスト型なので、演算子が使える.
    withCatList += wordList

withCatCount = collections.Counter(withCatList)
print(withCatCount.most_common()[:10])

word, count = zip(*withCatCount.most_common()[:10])
plt.bar(word, count)
plt.show()