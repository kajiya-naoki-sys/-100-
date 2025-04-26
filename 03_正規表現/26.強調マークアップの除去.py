import pandas as pd
import re

pattern = re.compile('\|(.+?)\s*=\s*(.+)')
#2個以上'が繰り返されるとき（強調されている時）それを消したい.
kyouchou = re.compile('\'{2,}(.+?)\'{2,}')
link = '~/Desktop/python/自然言語処理100本ノック/第3章_正規表現/jawiki-country.json'
df = pd.read_json(link, lines=True)
uk = df[df['title'] == 'イギリス'].text.values
ls = uk[0].split('\n')
dec = {}
for i in ls:
    r = re.findall(pattern, i)
    if r:
        #https://www.tohoho-web.com/ex/regexp.html#capture_group　を参照.
        #\\1で起きかけたとき、\1に置き換わる（1つ目の\によってエスケープシーケンスできて、\1になるから）.
        #【r = re.findall(kyouchou, i)】だと強調されている文字のみを抽出してしまう.
        #今回は強調された文字を削除して、強調されていない文字のみを抽出したい.
        #\1で強調した文字列のみ（強調された書式は取得しない）を取得して,強調された文字を強調されてない文字に置き換える.
        dec[r[0][0]] = re.sub(kyouchou, '\\1', r[0][1])
for i in dec:
    print(i + ':' +dec[i])