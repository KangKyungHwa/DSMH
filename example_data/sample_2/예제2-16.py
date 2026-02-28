import numpy as np
import pandas as pd

data = pd.DataFrame(pd.read_excel("..\데이터\고등학생_samples.xlsx"))

print('키의 범위 range : ', np.max(data.height)-np.min(data.height))
print('몸무게의 범위 range : ', np.max(data.weight)-np.min(data.weight),'\n')

print('키의 분산 variance : ', np.var(data.height))
print('몸무게의 분산 variance : ', np.var(data.weight),'\n')

print('키의 표준편차standard deviation : ', np.std(data.height))
print('몸무게의 표준편차standard deviation : ', np.std(data.weight))
