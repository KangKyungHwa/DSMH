import pandas as pd

df = pd.DataFrame(pd.read_excel("missing.xlsx"))
print(df)
df = df.dropna(axis=1)
print()
print(df)

