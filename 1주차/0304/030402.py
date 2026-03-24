# 변수 - 상수를 답는 그릇 (메모리의 이름)
name = "홍길동"
dept = "컴퓨터소프트웨어학과"
age = 24
height = 183.5
class1 = True
# 파이썬은 타입형을 사용하지 않음

print("이름: " + name)
print("학과: " + dept)

# + 기호는 문자열 과 문자열을 이어주므로 age와 같은 수를 담은 변수는 오류 발생
# , 기호룰 사용함으로써 문자열과 정수를 연결해줌 (문자열끼리도 , 사용해도 상관 X)
print("나이: " , age) 
print("신장: " , height)
print("오전반: " , class1)



print("이름: " + name)
print("학과: " + dept)

# + 기호 사용을 위해 정수/실수 변수를 문자열로 형변환
print("나이: " + str(age)) 
print("신장: " + str(height))
print("오전반: " + str(class1))


