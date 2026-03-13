import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')      # 라이브러리 sns에서 iris 데이터 불러오기 
iris.head()

sns.pairplot(iris, diag_kind='hist')    # 산점도 행렬 
plt.show()
