import pandas as pd
import numpy as np

df = pd.DataFrame(pd.read_excel("missing.xlsx"))
print(df)
print()
print('height=', df.height.mean())
print('weight=', df.weight.mean())
df = df.fillna(df.height.mean())
print()
print(df)





"""
print('height=', df.height.mean())
print('weight=', df.weight.mean())
print(df)
print('height=', df.height.mean())
print('weight=', df.weight.mean())
df = df.replace(0, np.nan)
print(df)

"""
