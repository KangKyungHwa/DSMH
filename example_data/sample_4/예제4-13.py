import pandas as pd
df = pd.DataFrame([
   ['20225001','A', 77],
   ['20225001','B', 80],
   ['20225002','A', 85],
   ['20225002','B', 82],
   ['20225003','A', 95],
   ['20225003','B', 90]],
    columns=['ID_num','Subject', 'Score'])
print(df, '\n')

df_pivot = df.pivot(index = 'ID_num', 
        columns='Subject', values = 'Score')
print(df_pivot, '\n')

df_pivot = df.pivot('ID_num','Subject').sum(1)
print(df_pivot, '\n')
