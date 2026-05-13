#map 내장함수 복습
print(pow(2,3))

#pow의 인자 값이 리스트면 오류 발생
# print(pow([1,2,3], [2,2,2]))

my_map = map(pow,[1,2,3],[2,2,2]) # 앞에 있는 리스트의 수 * 뒤에 있는 리스트의 수 
print(list(my_map))

def my_mult(x,y) :
    return x * y

print(list(map(my_mult, [1,2,3], [4,5,6])))

# 1 ~ 10까지의 값에 대해 my_mult를 실행하시오
print(list(map(my_mult, range(1,11), range(1,11))))

#문자열 각 조건에 맞게 판단하기
print(list(map(str.islower, 'python'))) #소문자
print(list(map(str.isupper, 'python'))) #대문자
print(list(map(str.isalpha, 'python'))) #영문

#map으로 형변환하기
print(list(map(int, [10, 10.4, '10'])))

print(int('10',2)) # 10을 2진수 취급
print(int('10',8)) # 10을 8진수 취급
print(int('10',16))# 10을 16진수 취급

print(list(map(int, ['1','5', '11'], [2,8,16])))
print(list(map(int, ['0','11', '15'], [2,8,16])))

print(str(10))
print(str(10.5))
print(list((map(str, [1,5,11]))))

print(list(map(int, map(str,[1,5,11]), [2,8,16])))
print(list(map(int, map(str,range(1,16)), [16]*15)))