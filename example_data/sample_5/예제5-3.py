import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset(('titanic'))

# 성별 생존여부
sns.countplot(data=df, x=df["sex"], hue=df["alive"])
plt.show()
#성별과 생존여부에 따른 교차표
print(pd.crosstab(df["sex"], df["alive"], margins=True))
print('\n')

