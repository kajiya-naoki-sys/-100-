import pandas as pd
import re

pattern = re.compile('\|(.+)\s*=\s*(.+)')
kyouchou = re.compile('\'{2,}(.+)\'{2,}')
mediaWiki = ['' for i in range(0, 2)]
mediaWiki[0] = re.compile('\[\[')
mediaWiki[1] = re.compile('\]\]')
link = '/workspace/03_正規表現/jawiki-country.json'
df = pd.read_json(link, lines=True)
uk = df[df['title'] == 'イギリス'].text.values
r = uk[0]
ls = uk[0].split('\n')
dec = {}
for i in ls:
    r = re.findall(pattern, i)
    if r:
        dec[r[0][0]] = re.sub(kyouchou, '\\1', r[0][1])
        num = r[0][1]
        for n in range(0, 2):
            num = re.sub(mediaWiki[n], '', num)
        dec[r[0][0]] = num
for i in dec:
    print(i + ':' + dec[i])
    print()