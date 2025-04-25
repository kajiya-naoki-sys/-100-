import pandas as pd
import json
url = '~/Desktop/python/自然言語処理100本ノック/第3章_正規表現/jawiki-country.json'
df = pd.read_json(url, lines=True)
uk = df[df['title'] == 'イギリス'].text.values
print(uk)