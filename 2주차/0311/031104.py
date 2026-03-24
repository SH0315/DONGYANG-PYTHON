#문자열 포멧
print("a" + 'b')
print('a', 'b') # 두 문자열 사이 공백 발생

print('ㅡ' * 10)

#방법1 (C언어 방식)
print("나는 %d살입니다" % 20)
print("나는 %.2f살입니다" % 178.9) # 소수점 두 자리
print("성별 %c입니다" % 'M')
print("나는 %s을 좋아해요" % "파이썬") # %s는 문자열로 변환해서 출력하므로 전부 %s로 해도 상관 X
#2개 값 이상의 내용 출력
print("나는 %s도 하고 %s도 할 수 있어요" %("파이썬", "자바")) # 여러개의 값을 출력할때는 %( ) 로 묶어서 출력

print('ㅡ' * 10)

#방법2 (문자열 format)
print("나는 {}살입니다".format(20))
print("나는 {}살입니다".format(178.9))
print("성별 {}입니다".format('M'))
#2개 값 이상의 내용 출력
print("나는 {}도 하고 {}도 할 수 있어요".format("파이썬", "자바"))
print("나는 {0}도 하고 {1}도 할 수 있어요".format("파이썬", "자바"))
print("나는 {1}도 하고 {0}도 할 수 있어요".format("파이썬", "자바")) # format값의 순서를 지정해서 출력가능

print('ㅡ' * 10)

#방법3 (format 함수와 변수지정)
print('이름은 {name}이고 {age}살입니다'.format(name = "소나무", age ='21'))
print("나는 키가 {height}cm이고 성별은 {gender} 입니다".format(height =178.9, gender = 'M'))

print('ㅡ' * 10)

#방법4 (f태그와 함수사용)
name = '소나무'
age = 21
height = 178.9
gender = 'M'
print(f'이름은 {name}이고 {age}살입니다')
print(f"나는 키가 {height:.2f}cm이고 성별은 {gender} 입니다")