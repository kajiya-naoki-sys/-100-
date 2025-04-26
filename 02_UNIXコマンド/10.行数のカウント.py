'''
pandasが最新のpythonに対応していないので、3.8でビルドすること
'''
import pandas as pd
url = 'https://nlp100.github.io/data/popular-names.txt'
#read_csvはdelimiterを適切に指定することで、csvファイル以外にも使える.今回は'\t'を指定してtsvファイルを読み込んでいる.また、heder=Noneでファイルの１行目がヘッダーになることを防いでいる.
df = pd.read_csv(url, delimiter='\t', header=None)
print(len(df))