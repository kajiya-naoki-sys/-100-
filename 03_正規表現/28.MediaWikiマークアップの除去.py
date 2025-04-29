import pandas as pd
import re

link = '/workspace/03_正規表現/jawiki-country.json'
df = pd.read_json(link, lines=True)
uk = df[df['title'] == 'イギリス']['text'].values
r = uk[0]
#https://www.javadrive.jp/python/regex/index17.html#section5 を参照.
#re.MULTILINEで.を使って複数行拾える. re.DOTALLdeで[.]に改行を含めることができる.
pattern = re.compile('^\{\{基礎情報 国(.*?)\n\}\}$', re.MULTILINE+re.DOTALL)
r = re.findall(pattern, r)
ls = r[0].split('\n')
dec = {}
for i in ls:
    pattern = re.compile('\|(.+?)\s*=\s*(.+)')
    r = re.findall(pattern, i)
    if r:
        pattern = re.compile('\'{2,}(.+)\'{2,}')
        dec[r[0][0]] = re.sub(pattern, '\\1', r[0][1])
        pattern = re.compile('\[\[')
        dec[r[0][0]] = re.sub(pattern, '', dec[r[0][0]])
        pattern = re.compile('\]\]')
        dec[r[0][0]] = re.sub(pattern, '', dec[r[0][0]])
        pattern = re.compile('\[\[ファイル(.+)\]\]')
        dec[r[0][0]] = re.sub(pattern, '', dec[r[0][0]])
        pattern = re.compile('<.+?>')
        dec[r[0][0]] = re.sub(pattern, '', dec[r[0][0]])
        pattern = re.compile('[\{\[]+.*?[\}\]]+')
        dec[r[0][0]] = re.sub(pattern, '', dec[r[0][0]])

for i, j in dec.items():
    print(i, ':', j)