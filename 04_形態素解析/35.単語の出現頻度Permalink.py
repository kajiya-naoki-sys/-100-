import collections

link = '/Users/kajiyanaoki/Desktop/python/自然言語処理100本ノック/第4章_形態素解析/neko.txt.mecab'
with open(link) as f:
    text = f.read().split('\n')
result = []
for i in text:
    if i == 'EOS' or i == '':
        continue
    ls = i.split('\t')
    tmp = ls[1].split(',')
    ##[表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音]
    d = {}
    d = {'surface': ls[0], 'base': tmp[6], 'pos': tmp[0], 'pos1': tmp[1]}
    result.append(d)

wordList = []
for i in result:
    #記号の時は除外.
    if i['pos'] == '記号':
        continue
    wordList.append(i['base'])
#!collectionsライブラリのCounterでリスト内の重複要素を数える.
wordCount = collections.Counter(wordList)
#!collectionsライブラリの.most_common()でスライスが使えるようにする.
print(wordCount.most_common()[:50])