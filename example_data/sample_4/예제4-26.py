import pandas as pd

df = pd.DataFrame(pd.read_excel("missing.xlsx"))
print(df)
df = df.dropna(axis=0)
print()
print(df)

