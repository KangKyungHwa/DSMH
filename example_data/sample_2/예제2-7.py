# 주어진 두 숫자의 평균을 반환하는 함수
def avr(a, b):
  sum = a + b
  return sum/2

a = int(input('정수 a를 입력하고 Enter: '))
b = int(input('정수 b를 입력하고 Enter: '))

result = avr(a, b)
print(result)
