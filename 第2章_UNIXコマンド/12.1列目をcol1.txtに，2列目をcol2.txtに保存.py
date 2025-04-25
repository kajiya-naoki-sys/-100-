import pandas as pd
url = 'https://nlp100.github.io/data/popular-names.txt'
df = pd.read_csv(url, delimiter='\t', header=None)
df[0].to_csv('col1.txt', header=False, index=False)
df[1].to_csv('col2.txt', header=False, index=False)