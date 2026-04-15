#익명 함수
#간단한 함수를 한줄로 정의하는 방법
#lamda 키워드를 사용하여 정의
#주로 다른 함수에 인자로 전달하거나, 간단한 연산을 수행하는데 사용

#lambda 매개변수 : 표현식

lambda : print('안녕')
(lambda : print('안녕'))()

my_hello = lambda : print('안녕')
my_hello()

#평수를 매개변수로 받아 그것을 제곱미터로 변환
def toArea(pg) :
    return pg * 3.3

print(toArea(24))


#위의 함수를 람다 함수로 정의하면? 
lambda pg : pg * 3.3

#정의한 람다 함수 호출하기
print((lambda pg : pg * 3.3)(24))

#다른 방법으로 정의해서 출력
my_pg = lambda pg : pg * 3.3
print(my_pg(24))


add1 = lambda x : x + 1
a = 10
print(add1(a))


#람다 함수 응용하기
#일반적인 정렬
subject = ['basic', 'kotlin', 'java', 'python', 'C', 'C++']
print(sorted(subject))
#문자길이로 정렬
sorted_len = sorted(subject, key = len)
print(sorted_len)

#람다함수로 정렬
p1= [ ('basic', 1964), ('java', 1995), ('kotlin', 2016), ('python', 1991), ('c', 1973)]

# 이름 순 정렬
print(sorted(p1,key = lambda lang: lang[0]))

# 연도 순 정렬
print(sorted(p1,key = lambda lang: lang[1])) 

# 이름길이 순 정렬
print(sorted(p1, key = lambda lang : len(lang[0])))

print(sorted(p1))