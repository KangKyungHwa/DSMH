import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#타이타닉 데이터 불러오기
#1데이터 변수 정보 출력
df = sns.load_dataset(('titanic'))
print(df.info())
print(df.head())

# 데이터의 상위 5행을 출력
pd.set_option('display.max_columns', None)
print(df.head())
