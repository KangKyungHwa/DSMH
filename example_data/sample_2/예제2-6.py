# 주어진 숫자만큼 문자를 반복
def rept(string, n):
   n_st=''
   for i in range(n): 
     n_st = n_st + string
   print(n_st)

string = input('문자를 입력하고 Enter: ')
n = int(input('정수숫자를 입력하고 Enter: '))

rept(string, n)
