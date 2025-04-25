import pandas as pd
col1 = pd.read_csv('col1.txt', header=None)
col2 = pd.read_csv('col2.txt', header=None)
df = pd.concat([col1, col2], axis=1)
df.to_csv('col1_2.txt', sep='\t', header=False, index=False)