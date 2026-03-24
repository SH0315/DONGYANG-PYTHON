#자료구조의 변경
menu = { "커피", "우유", "주스"}
print(menu, type(menu))

#리스트로 형변환
menu = list(menu)
print(menu, type(menu))

#투플로 형변환
menu = tuple(menu)
print(menu, type(menu))

#세트로 형변환
menu = set(menu)
print(menu, type(menu))


# 퀴즈 코드
from random import *
users = range(1,21) #range는 끝 숫자 전까지만
users = list(users)
print(users)
shuffle(users)
winners = sample(users,4)
print(winners)