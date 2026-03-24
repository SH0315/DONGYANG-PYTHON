# Quiz) 학교에서 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈이 shuffle과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# --  축하합니다 --

# (활용예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst) #무작위로 변경함
# print(lst)

from random import *
# users = range(1,21)
# users = list(users)
# shuffle(users)
# winners = sample(users,4)
# print("--당첨자 발표--")
# print(f"치킨 당첨자 : {(winners[0:1])}")
# print(f"커피 당첨자 : {(winners[1:])}")
# print("--축하 합니다--")



#학생들을 2명씩 랜덤으로 팀을 만들어서 딕셔너리 형태로 저장하시오.
# random.sample() 사용할 것
# 한 학생은 한 번만 사용 (중복 X)

# 결과는 이런 형태로 만들기
# {
#     "1팀": ["지현", "준호"],
#     "2팀": ["민수", "서연"],
#     ...
# }

from random import *
students = ["민수", "지현", "수빈", "영호", "지우", "서연", "준호", "예린"]
teams = {}
teamcount = 1

while len(students) > 0 :
    selected = sample(students,2)
    teams[f"{teamcount}팀"] = selected
    for s in selected :
        students.remove(s)
        
    teamcount += 1

print(teams)




