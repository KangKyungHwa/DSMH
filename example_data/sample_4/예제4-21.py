import pandas as pd

df = pd.DataFrame(pd.read_excel("missing.xlsx"))
print(df.isnull().sum())

