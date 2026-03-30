import pandas as pd
df_x = pd.DataFrame(
        [['A', 1],
         ['B', 2],
         ['C', 3]],
        columns=['x1', 'x2'])
print(df_x, '\n')

df_y = pd.DataFrame(
        {"x1" : ['B', 'C', 'D'],
         "x3" : [2, 3, 4]})
print(df_y, '\n')

print(pd.merge(df_x, df_y, how='left'), '\n')

print(pd.merge(df_x, df_y, how='right'), '\n')

print(pd.merge(df_y, df_x))
