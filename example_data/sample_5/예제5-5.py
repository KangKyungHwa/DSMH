import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset(('titanic'))

# 성별에 따른 나이분포 
g = sns.FacetGrid(df,col='sex')
g.map(plt.hist,'age')
plt.show()

# 생존여부에 따른 나이분포 
g = sns.FacetGrid(df, col='sex', row='alive')
g.map(plt.hist,'age')
plt.show()

# 객실등급별 나이분포 
g = sns.FacetGrid(df, col='class')
g.map(plt.hist,'age')
plt.show()

# 객실 등급별 생존여부에 따른 나이 분포
g = sns.FacetGrid(df, col='class', row='alive')
g.map(plt.hist,'age')
plt.show()

