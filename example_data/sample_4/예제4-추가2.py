import pandas as pd
df = pd.DataFrame([
   ['20225001','A', 77],
   ['20225001','B', 80],
   ['20225002','A', 85],
   ['20225002','B', 82],
   ['20225003','A', 95],
   ['20225003','B', 90]],
    columns=['ID_num','Subject', 'Score'])

fdv1 = pd.pivot_table(df, index='Subject', values='Score')
print(fdv1)

print('\n')
fdv2 = pd.pivot_table(df, index='ID_num', columns = 'Subject', values='Score')
print(fdv2)
