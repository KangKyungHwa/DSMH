import pandas as pd
import matplotlib.pyplot as plt
# 엑셀 파일 불러오기  참고 
data = pd.DataFrame(pd.read_excel("..\데이터\고등학생_samples.xlsx"))

plt.hist(data.height, label='bins=10', bins=10) #막대수 10개로 하고 레이블 작성
plt.legend()
plt.show()
