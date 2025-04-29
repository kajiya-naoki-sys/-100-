import pandas as pd
import json
url = '/workspace/03_正規表現/jawiki-country.json'
df = pd.read_json(url, lines=True)
uk = df[df['title'] == 'イギリス'].text.values
print(uk)