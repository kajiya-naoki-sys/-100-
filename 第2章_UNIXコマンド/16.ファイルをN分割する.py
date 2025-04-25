import pandas as pd
url = 'https://nlp100.github.io/data/popular-names.txt'
N = int(input())
df = pd.read_csv(url, delimiter='\t', header=None)
#切り上げ除算（余があったら繰り上げる）を用いる.
step = (len(df) + N - 1) // N
for i in range(N):
    df_split = df.iloc[step*i:step*(i+1)]
    df_split.to_csv(f'df_split{i}.txt', sep='\t', header=False, index=False)