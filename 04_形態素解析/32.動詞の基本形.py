link = '/workspace/04_形態素解析/neko.txt.mecab'
with open(link) as f:
    text = f.read().split('\n')
result = []
for i in text:
    if i == 'EOS':
        continue
    if i == '':
        continue
    ls = i.split('\t')
    tmp = ls[1].split(',')
    #[表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音]
    if tmp[0] != '動詞':
        continue
    result.append(tmp[6])
print(result)