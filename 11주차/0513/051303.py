#콤마가 삽입된 문자열 원화를 정수로 변환
def to_int(num):
    return int(num.replace(',',''))

wons = ['1,100', '100,000', '1,000,000']
print(list(map(to_int, wons)))

#람다 함수로 표현
print(list(map(lambda s : int(s.replace(',','')), wons)))


# 1차원 배열을 2차원 배열로 변환
langs = ['java', 'python', 'c/c++', 'kotlin']
print(list(map(list,langs)))

langs = 'java'
print(list(map(list,langs)))
