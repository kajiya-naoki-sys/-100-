import pandas as pd
#正規表現を知りするためのライブラリをインポート.
import re

#reライブラリで対象とする文字列を正規表現にする処理のためにはまずコンパイルする.コンパイルすることで、その文字列を正規表現として扱える.
#引数には正規化したい文字列をいれる.
pattern = re.compile('Category')
url = '~/Desktop/python/自然言語処理100本ノック/第3章_正規表現/jawiki-country.json'
df = pd.read_json(url, lines=True)
uk = df[df['title'] == 'イギリス'].text.values
ls = uk[0].split('\n')
for i in ls:
    #serchで正規表現を対象の文字列から検索、一番初めのを抽出できる.
    #第一引数には正規表現を、第二引数には対象文字列を入れる.
    if re.search(pattern, i):
        print(i)
