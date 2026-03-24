#랜덤 함수 사용
from random import *
print(random()) # 0.0 에서 1.0 미만 사이의 수를 출력
print(random() * 10) # 0.0 에서 10.0 미만 사이의 수를 출력
print(int(random() * 10)) # 0 에서 10 미만 사이의 수를 출력
print(int(random() * 10) + 1) # 1이상 10이하
print(int(random() * 45) + 1)
print(randrange(1,46)) # 1 ~ 45 이하 (시작값 없을시에는 0으로 시작)
print(randint(1,45)) # 1 ~ 45이하

