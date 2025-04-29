import pandas as pd
import re


#https://note.nkmk.me/python-str-extract/#_6 を参照.
#1回以上の=で始まり、1回以上の=で終わる文字列.
#'^'…文頭. '=+'…1つ以上の=, '.#'…0個以上の改行以外の文字列が入る, '$'…文末.
pattern = re.compile('^=+.*=+$') 
link = '/workspace/03_正規表現/jawiki-country.json'
df = pd.read_json(link, lines=True)
uk = df[df['title'] == 'イギリス'].text.values
for i in range(0, len(uk)): 
    ls = uk[0].split('\n')
    for j in ls:
        if re.search(pattern, j):
            level = (j.count('=') // 2) - 1
            j = j.replace('=', '')
            print(j, level)