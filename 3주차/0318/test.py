# 문제: 과일 개수 세기

# 리스트가 주어진다
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

# 해야 할 것:
# 각 과일이 몇 번 나왔는지 세어서 딕셔너리로 출력하시오

# 결과 예시:
# {
#     "apple": 3,
#     "banana": 2,
#     "orange": 1
# }

# 조건:
# 1. 미리 딕셔너리 만들지 말 것
# 2. 반복문 사용할 것
# 3. append() 사용 금지 (숫자 세기)
# 4. 딕셔너리에 없는 키가 나오면 직접 처리할 것

# 여기에 코드 작성 👇
result = {}

for s in fruits :
  if s not in result :
    result[s] = 1
  else :
    result[s] += 1

print(result)



    

