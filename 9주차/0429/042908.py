# map 함수 : 반복가능한 iteralbe 객체를 받아서 각 요소에 함수를 적용해주는 함수
def add_1(n) :
    return n + 1

target = [1,2,3,4,5]

result = map(add_1, target)
# 일반 출력은 결과가 이터레이터 형태이므로 리스트나 투플로 형 변환해서 출력해야함
print(result)
print(f'일반함수로 출력 : {list(result)}')


# 재사용 목적이 없으면 lambda함수를 적용해서 간소화
result = map(lambda x : x + 1, target)
print(f'람다함수로 출력 : {list(result)}')
