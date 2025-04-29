import pandas as pd
import re

pattern = re.compile('\|(.+?)\s=\s*(.+)')

link = '/workspace/03_正規表現/jawiki-country.json'
df = pd.read_json(link, lines=True)
uk = df[df['title'] == 'イギリス'].text.values
ls = uk[0].split('\n')
dec = {}
for i in ls:
    r = re.findall(pattern, i)
    if r:
        dec[r[0][0]] = r[0][1]
for i in dec:
    print(i + ':' + dec[i])