import pandas as pd
from matplotlib import pyplot as plt
data = pd.DataFrame(pd.read_excel("..\데이터\휘발유_우유가격변화.xlsx"))

x = data.year
y1 = data.gasoline
y2 =data.milk

plt.plot(x, y1, linestyle='solid', label='gasoline')  # x와 y1 그래프 작성
plt.plot(x, y2, linestyle='dashed', label='milk')  # x와 y2 그래프 작성

plt.legend(loc='best', ncol=2)                # 레이블 표시 방법 
plt.title('change of price')   
plt.show()	              
