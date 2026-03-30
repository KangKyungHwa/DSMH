# 프로그램 1
import pandas as pd
df1 = pd.DataFrame(
        [[1, 4],
         [2, 5],
         [3, 6]],
        columns=['a', 'b'])
print(df1, '\n')

df2 = pd.DataFrame(
        {"c" : [7, 8, 9],
         "d" : [10, 11, 12]})
print(df2, '\n')

#프로그램 2
df3 = pd.melt(df1)
print(df3)

