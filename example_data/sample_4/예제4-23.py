import pandas as pd

df = pd.DataFrame(pd.read_excel("missing.xlsx"))
print('height=', df.height.mean())
print('weight=', df.weight.mean())
