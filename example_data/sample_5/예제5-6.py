import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset(('titanic'))

# 도시별 탑승인원
sns.countplot(df, x='embark_town')
plt.show()

# 탑승 도시별 성별구분
sns.countplot(df, x='embark_town', hue='sex')
plt.show()

# 탑승 도시별 성별구분
sns.countplot(df, x='embark_town', hue='alive')
plt.show()

# 탑승 도시별 등급별 구분
sns.countplot(df, x='embark_town', hue='class')
plt.show()

#도시별 성별 생존여부의 사례수
print(pd.crosstab(df["alive"], [df["embark_town"], df["sex"]], margins=True))
print('n')
#도시별 등급별 생존여부의 사례수
print(pd.crosstab(df["alive"], [df["embark_town"], df["pclass"]], margins=True))



