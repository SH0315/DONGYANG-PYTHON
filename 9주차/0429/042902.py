# 2개의 리스트나 튜플로 키-값 항목인 딕셔너리를 생성
# 1) 2개의 리스트 만들기
names = ['강바람', '민들레', '들국화']
age = [25, 22,24]

# 2) ZIP함수 사용해 리스트를 뎍셔너리로 변환
user_info = dict(zip(names,age))

# 3) 사용자 정보 출력
for names, age in user_info.items() :
    print(f'{names} : {age}')
print("ㅡ" * 20)
    
# 4) 사용자 정보 딕셔너리에 추가
user_info['소나무'] = 25
print(user_info)
print("ㅡ" * 20)

# 5) 사용자 정보 수정
user_info['강바람'] = 23
for names, age in user_info.items() :
    print(f'{names} : {age}')
print("ㅡ" * 20)
    
# 6) 사용자 정보 삭제 (민들레 삭제)
if '민들레' in user_info :
    del user_info['민들레']

for names, age in user_info.items() :
    print(f'{names} : {age}')
print("ㅡ" * 20)
    
# 7) 모든 사용자의 나이의 총합
total_age = sum(user_info.values())
print(f'총 나이 : {total_age}')

