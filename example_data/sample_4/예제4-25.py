import pandas as pd
import numpy as np

df = pd.DataFrame(pd.read_excel("missing.xlsx"))
print(df)
df = df.replace(0, np.nan)
print()
print(df)

