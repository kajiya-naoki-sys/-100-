import pandas as pd
url = 'https://nlp100.github.io/data/popular-names.txt'
df = pd.read_csv(url, delimiter='\t', header=None)
vc = df[0].value_counts()
vc = pd.DataFrame(vc)
vc = vc.reset_index()
vc.columns = ['name', 'count']
vc = vc.sort_values(by=['count', 'name'], ascending=[False, False])
print(vc)