import pandas as pd
import re

df = pd.read_csv('data/BRCA.txt.gz', sep = '\t', index_col = 0)

with open('data/selected-genes.txt') as f:
  filter = f.read().strip()

filter = set(filter.split('\n'))

selected = list()

for idx in df.index:
  if re.sub('\\|.*', '', idx) in filter:
    selected.append(idx)

filtered = df.loc[selected]

print 'Saving...'

filtered.to_csv('data/BRCA-filtered.txt.gz', sep = '\t', compression = 'gzip')
