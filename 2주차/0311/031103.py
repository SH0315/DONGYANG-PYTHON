#문자열 함수
python = "Python is Fun"
print(python)
print(python.lower()) # 모든 글자를 소문자로
print(python.upper()) # 모든 글자를 대문자로

# isupper / islower 사용시는 결과값이 Boolean 값으로 나옴 (true / false)
print(python[0].isupper()) 
print(len(python)) # 문자열의 길이 출력
print(python.replace("Python", "Java")) # replace 사용시 글자열이 변환되어 출력

# 글자의 위치 찾기 
i = (python.index("n", 0))
print("첫번째 n은 : " + str(i) )
i=  python.index("n", i+1) # 처음 찾은 위치 다음 위치부터 찾으라는 뜻
print("두번째 n은 : " + str(i))

j = python.find('n')
print("첫번째 n은 : " + str(j))
j = python.find('n', j + 1)
print("두번째 n은 : " + str(j))

#index와 find의 차이점
print(python.find("Java")) # - 해당 문자열이 없으면 -1 출력
#print(python.index("Java")) # 해당 문자열이 없으면 오류 발생

#문자갯수
print(python)
print(python.count('n')) # 대소문자 따로 취급



 