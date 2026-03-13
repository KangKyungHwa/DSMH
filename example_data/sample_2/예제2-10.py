from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

ratio = [46.0, 30.0, 13.6, 8.7, 1.7]    # 퍼센트 비율 (전체 합은 100)
labels = ['고향 및 부모친척방문', '집에서 휴식', '국내여행', '국외여행', '기타']  #레이블 
plt.pie(ratio, labels=labels, autopct='%.1f%%')  # 퍼센트의 표시 방법 
plt.show()
