import pandas as pd
url = 'https://nlp100.github.io/data/popular-names.txt'
df = pd.read_csv(url, delimiter='\t', header=None)
#byでソートの対象カラムを指定、ascending True/Falseで昇順/降順を指定.
n_df = df.sort_values(by=2,ascending=False)
print(n_df)