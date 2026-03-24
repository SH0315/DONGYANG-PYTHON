#연산자와 함수 응용
#연산자의 종류: 산술, 관계, 논리,  
#산술 연산자(+, -, *, /(몫과 나머지) , //(몫), %(나머지))
#관게 연산자(==, !=, <, <= , >, >=)
#논리 연산자(and , or , not)
from math import *
print(2 + 3 * 4)
print((2 + 3) * 4)
print(10/3)
print(10//3)
print(10%3)

print("-"*20)
print(3==5)
print(3!=5)

print("-"*20)
print(3==5 and 3>2)
print(3==5 or 3>2)

#함수
print(abs(-5)) #절댓값
print(pow(4,2)) # 제곱
print(max([1,2,3,4,5,6])) # 최대값
print(min(1,2)) #최소값
print(floor(4.99)) # 4.99를 넘지않는 최대값
print(ceil(3.14)) # 3.14를 넘는 최대값
print((sqrt(16)))   # 루트 적용한 실수 형태의 값
print(int(sqrt(16)))
