import pandas as pd
import re

pattern = re.compile('Category')
link = '~/Desktop/python/自然言語処理100本ノック/第3章_正規表現/jawiki-country.json'
df = pd.read_json(link, lines=True)
uk = df[df['title'] == 'イギリス'].text.values
ls = uk[0].split('\n')
for i in ls:
    if re.search(pattern, i):
        i = i.replace('[[Category:', '').replace('|', '').replace('*', '').replace(']]', '')
        print(i)