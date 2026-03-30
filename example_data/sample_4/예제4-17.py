import pandas as pd
file_data = pd.read_csv("..\데이터\sample1.csv")
print(file_data[0:5])
total_score = file_data['점수'] * 5 + file_data['출석']
new_data = [file_data['이름'], total_score]

#axis=0는 위+아래로, axis=1은 왼쪽+오른쪽으로 합치기 
result = pd.concat(new_data, axis=1, keys=['name', 'total'])  

print(result)                    #[결과 1] 참고
result.to_csv("result1.csv")     #[결과 2] 참고 
result.to_excel("result1.xlsx")  #[결과 3] 참고 

#추가된 내용(추가.py)
import matplotlib.pyplot as plt
plt.hist(total_score, label='score data', bins=7)
plt.legend()
plt.savefig("histogram of score.png")
plt.show()

