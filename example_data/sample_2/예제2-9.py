from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

x=[ '보조출연.방청', '방문.학습지 교사', '컴퓨터.정보통신', '교육.강사 기타', '요가.필라테스 강사']
y=[29874, 23551, 20812, 19930, 19766] 

x1=[ '커피전문점',  '캐셔.카운터', '베이커리.도넛.떡', '아이스크림.디저트', '편의점']
y1=[9411, 9371, 9354, 9317, 9268]

plt.bar(x, y)                    # x축과 y축의 데이터     
plt.title('아르바이트 상위시급')   # 제목 표시
plt.xticks(rotation=20)          #x축 레이블 회전  
plt.show()

plt.barh(x1, y1)
plt.title('아르바이트 하위시급')
plt.show()
