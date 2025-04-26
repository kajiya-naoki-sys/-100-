import pandas as pd
url = 'https://nlp100.github.io/data/popular-names.txt'
N = int(input())
df = pd.read_csv(url, delimiter='\t', header=None)
print(df.tail(N))