s = [1,5,11]
print(s[::])  # 전체출력
print(s[::-1]) # 역순 전체출력

# map 응용 - 문자열을 역순과 대문자로 변환
def  my_reverse(s) :
    return (s[::-1])

langs = ['java', 'python', 'c/c++', 'koltin']
print(list(map(my_reverse, langs)))

#람다 함수로 표현
print(list(map(lambda s : s[::-1] ,langs)))
#람다 함수 이용해서 대문자로 표현
print(list(map(lambda s : s.upper(), langs)))

#첫글자를 대문자로
print(list(map(str.capitalize, langs)))
