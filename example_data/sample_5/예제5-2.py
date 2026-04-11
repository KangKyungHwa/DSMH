import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset(('titanic'))

#생존자와 사망자 사례수 
print(df["survived"].value_counts())
print(df["alive"].value_counts())
# 생존여부 구성비 (원그래프)
plt.pie(df["alive"].value_counts(), labels=['no', 'yes'], explode=(0, 0.1) , startangle = 90, shadow=True, autopct='%.1f')
plt.show()
print('\n')

#성별  사례수 확인
print(df["sex"].value_counts())
# 성별 구성비 (원그래프)
plt.pie(df["sex"].value_counts(), labels=['male', 'female'], explode=(0, 0.1) , startangle = 90, shadow=True, autopct='%.1f')
plt.show()
print('\n')

# 성별, 아이별 사례수
print(df["who"].value_counts())
#  성별, 아이별 구성비 (원그래프)
plt.pie(df["who"].value_counts(), labels=['man', 'woman', 'child'], startangle = 90, shadow=True, autopct='%.1f')
plt.show()
print('\n')

# 탑승 도시(국가)별 사례수
print(df["embark_town"].value_counts())
#  탑승 도시(국가)별 구성비 (원그래프)
plt.pie(df["embark_town"].value_counts(), labels=['Southampton', 'Cherbourg', 'Queenstown'], startangle = 90, shadow=True, autopct='%.1f')
plt.show()
print('\n')

# 객실 등급별 사례수 
print(df["class"].value_counts())
# 객실 등급별 구성비 
plt.pie(df["class"].value_counts(), labels=['Third', 'First', 'Second'], startangle = 90, autopct='%.1f')
plt.show()
print('\n')

# 혼자 탑승 여부에 따른 사례수와 그래프 
print(df["alone"].value_counts())
plt.pie(df["alone"].value_counts(), labels=['True', 'False'], startangle = 90, shadow=True, autopct='%.1f')
plt.show()
print('\n')

#나이분포와 요금분포 
sns.histplot(df, x='age', bins = 8)
plt.show()
sns.histplot(df, x='fare', bins = 10)
plt.show()
