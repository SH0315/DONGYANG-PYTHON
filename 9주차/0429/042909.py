#filter 함수 : map함수와 동일하나 특정 조건을 걸러서 걸러진 요소들로 이터레이터 객체를 만들어 리턴
target = [1,2,3,4,5,6,7,8,9,10]

def is_even(n) :
    return True if n % 2 == 0 else False

result = filter(is_even,target)
print(f'일반함수로 출력 : {list(result)}')

result = filter(lambda x : x % 2 == 0, target)
print(f'람다함수로 출력 : {list(result)}')

