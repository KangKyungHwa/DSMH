import numpy as np 
import pandas as pd
from scipy import stats

x = pd.read_excel("..\데이터\중학생_남자_몸무게.xlsx")

# 평균 계산  
print('mean = ', np.average(x), '\n')

# 중앙값 계산
print('median =', np.median(x),'\n')

# 최빈값 계산
print('mode =', stats.mode(x))

