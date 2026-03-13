import pandas as pd
from scipy import stats

data = pd.DataFrame(pd.read_excel("..\데이터\고등학생_samples.xlsx"))

print(data.describe())

print(stats.describe(data))

