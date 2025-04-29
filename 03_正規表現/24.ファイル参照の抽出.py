import pandas as pd
import re

#https://www-creators.com/archives/2612 を参照
#'File'または'ファイル:(.+)|', \で直後(|)をエスケープシーケンス.
#()内を取り出すことができる.
pattern = re.compile('File|ファイル:(.+)\|')
file = re.compile('(.*?\..{3})')
link = '/workspace/03_正規表現/jawiki-country.json'
df = pd.read_json(link, lines=True)

#https://note.nkmk.me/python-pandas-str-contains-match/#isin を参照
#pandasの要素完全一致の探し方.
uk = df[df['title'] == 'イギリス'].text.values
#print(df.title.values)みたいに【[DataFrame].[カラム名].values】で要素を取り出す.
#∴df[df['カラム名'] == '文字列']は一つのDataFrameである.

ls = uk[0].split('\n')
for i in ls:
    #re.serchでなくre.findallだと一致するものを全て抽出.
    if re.findall(pattern, i):
        i = re.findall(pattern, i)
        i = re.findall(file, i[0])
        print(i[0])