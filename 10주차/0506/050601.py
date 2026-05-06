def power(item) :
    return item * item

def under_3(item) :
    return item < 3

list_input_a = [1,2,3,4,5]

output_a = map(power,list_input_a)
print("map()함수의 실행결과")
print("map(power, list_input_a) : ", output_a)
print("map(power, list_input_a) : ", list(output_a))

#람다 함수로 출력
lambda_a = map(lambda item : item * item , list_input_a)
print(f'람다함수로 출력 : {list(lambda_a)}')
print()

output_b = filter(under_3, list_input_a)
print("filter()함수의 실행결과")
print("filter(under_3, list_input_a) : ", output_b)
print("filter(under_3, list_input_a) : ", list(output_b))

#람다 함수로 출력
lambda_b = filter(lambda item : item < 3 , list_input_a)
print(f'람다함수로 출력 : {list(lambda_b)}')



