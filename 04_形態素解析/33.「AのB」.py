link = '/workspace/04_形態素解析/neko.txt.mecab'
with open(link) as f:
    text = f.read().split('\n')
buf = []
d = {}
for i in text:
    if i == 'EOS':
        continue
    if i == '':
        continue
    ls = i.split('\t')
    tmp = ls[1].split(',')
    d = {'surface': ls[0], 'pos': tmp[0]}
    buf.append(d)
result = []
for i in range(1, len(buf)-1):
    if buf[i-1]['pos'] == '名詞' and buf[i]['surface'] == 'の' and buf[i+1]['pos'] == '名詞':
        result.append(buf[i-1]['surface'] + buf[i]['surface'] + buf[i + 1]['surface'])

#set()で重複を消す.
result = list(set(result))        
print(len(result))