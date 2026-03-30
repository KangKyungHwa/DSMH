# 프로그램 3
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

df4 = pd.concat([df1, df1], axis=0)
print(df4, '\n')

df4 = pd.concat([df1, df1], axis=1)
print(df4, '\n')

df5= pd.concat([df1, df2], axis=0)
print(df5, '\n')

df6 = pd.concat([df1, df2], axis=1)
print(df6, '\n')
