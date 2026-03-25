# 반복문 for in 형식이고 다음 리스트, 범위 값이 나올 수 있음
for n in [1,2,3,4,5] :
    print(f"{n}번 출석했나요?")

for n in range(1,6) :
    print(f"{n}번 출석했나요?")
    
#문자열과 반복문
#standby에 "강바람", "들국화", "채송화", "소나무" 리스트로 저장하고 반복문을 이용해 이름들을 출력

standby = ["강바람", "들국화", "채송화", "소나무"]

for name in standby :
    print(f"{name} 님 입장하세요")
    
for c in "python" :
    print(f"{c}", end= '    ')
    
#딕셔너리와 반복문
pl_dict = {'basic': 1964, 'java':  1995, 'kotlin' : 2016, 'python' : 1991 ,  'c' : 1973}

# 키 값이 순차적으로 name 변수에 저정되고 출력됨 -> 키 값 출력
for name in pl_dict :
    print(name)
#키 값이 순차적으로 name 변수에 저정되고 키가 name인 밸류 값이 출력됨 -> 밸류값 출력
for name in pl_dict :
    print(pl_dict[name])    
        
for name, year in pl_dict.items():
    print(f"{name} 언어의 출시연도는 {year}입니다.")
