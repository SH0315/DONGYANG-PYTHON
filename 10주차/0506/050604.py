# 자주 사용하는 코딩 3
from datetime import date
from datetime import datetime

#실습 1
print(10 - (3<5)) # TRUE라서 값이 1이기 때문에 9가 나옴
print(10 - (3>5)) # FALSE 라서 값이 0이기 때문에 10이 나옴

#실습 2 (순서대로 비교해서 전부 참이면 TRUE 아니면 FALSE)
print((100,1) < (100,2))
print((101,2,3) < (100,2,0))

#실습 3
t = date.today()
c = date(2026,5,8)
print(c-t)
print(abs(c-t))
print(abs(c-t).days) 

#실습 4 (주민번호 입력받아 만 나이 구하기)
def calculate_age(jumin_number):
    today = datetime.now()
    
    birth_year = 0
    birth_month = int(jumin_number[2:4])
    birth_day = int(jumin_number[4:6])
    
      
    if int(jumin_number[7]) <= 2:
        birth_year = 1900 + int(jumin_number[0:2])
    else:
        birth_year = 2000 + int(jumin_number[0:2])
                                    
                                     #생일 안 지났으면 -1  
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
      

    return age

jumin = input('주민등록번호를 입력하세요 : ')
result = calculate_age(jumin)
print(f'만 나이는 {result}세입니다.')
