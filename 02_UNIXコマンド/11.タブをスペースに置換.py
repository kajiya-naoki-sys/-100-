import pandas as pd
url = 'https://nlp100.github.io/data/popular-names.txt'
#\tはタブの正規表現.
df = pd.read_csv(url, delimiter='\t', header=None)
df.to_csv('space.txt', sep=' ', header=False, index=False)