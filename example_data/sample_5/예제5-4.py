import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset(('titanic'))

#객실등급별 생존여부
sns.countplot(data=df, x=df["class"], hue=df["alive"])
plt.show()
#객실등급별 생존여부에 따른 교차표
print(pd.crosstab(df["class"], df["alive"], margins=True))
print('n')

#객실등급별 성별인원
sns.countplot(data=df, x=df["class"], 
hue=df["sex"])
plt.show()
#객실등급별 성별에 따른 교차표
#생존여부에 따른 객실등급과 성별의 교차표
print(pd.crosstab(df["alive"], [df["class"], df["sex"]], margins=True))
print('n')

# 객실 등급별 성별 생존율
sns.catplot(x='class', y= 'survived', col= 'sex', data=df, kind='bar')
plt.show()





