import pandas as pd


df = pd.DataFrame([[0, 1], [1, 0]])

print(str(df[df.columns[0]].sum()) + ' is the sum of the first column')