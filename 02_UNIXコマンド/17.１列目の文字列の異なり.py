import pandas as pd
url = 'https://nlp100.github.io/data/popular-names.txt'
df = pd.read_csv(url, delimiter='\t', header=None)
set_df = set(df[0])
unique_df = df[0].unique()
'''
print(set_df)
print(type(set_df))
print(unique_df)
print(type(unique_df))
'''

#setクラスの戻り値にはsortは使えない.
#set_df = set_df.sort()
set_df = sorted(set_df)

for i in set_df:
    print(i)