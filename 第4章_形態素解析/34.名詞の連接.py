link = '/Users/kajiyanaoki/Desktop/python/自然言語処理100本ノック/第4章_形態素解析/neko.txt.mecab'
with open(link) as f:
    text = f.read().split('\n')
buf = []
d = {}
for i in text:
    if i == 'EOS' or i == '':
        continue
    ls = i.split('\t')
    tmp = ls[1].split(',')
    ##[表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音]
    d = {'surface': ls[0], 'pos': tmp[0]}
    buf.append(d)

result = []
temporary = ''
flag = 0
count = 0
for i in buf:
    if i['pos'] == '名詞':
        #print(i)
        count += 1
        flag = 1
        temporary += i['surface']
    else:
        if flag == 1:
            #最長一致だから名詞が1文字のみの時は数えない.
            if(count > 1):
                result.append(temporary)
            temporary = ''
            count = 0
            flag = 0

result = list(set(result))
print(len(result)) 
print(result)