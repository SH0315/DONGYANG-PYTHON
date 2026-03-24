#딕셔너리() : 키와 값의 쌍으로 이루어짐
members = {1 : "강바람" , 2 : '민들레', 3 : '들국화' }
print(members[1])
print(members[2])
print(members.get(1))
print(members.get(2))


#index와 get의 차이
#print(members[5])               #오류 발생
print(members.get(5))           # NONE 출력


#응용문제
#키가 5인 값을 출력하되 없으면 "키가 5인 값 없음"
if (members.get(5)) :
    print(members.get(5))
else :
    print("키가 5인 값 없음")   
    
#키가 5인 값을 출력하되 없으면 키5에 "비어있음"
print(members.get(5, '비어있음'))
    

#member에 있는 지 확인하기   
print(3 in members)
print(5 in members) 

#members 에 추가하기
#4로 소나무 추가
members[4] = '소나무'
print(members)

#소나무 삭제
del members[4]
print(members)

# 키 값/ 밸류 값 출력
print(members.keys()) # 키 값만 출력 
print(members.values()) # 밸류 값만 출력
print(members.items()) # 키 값과 밸류 값 쌍으로 출력

#딕셔너리 내용 지우기
print(members.clear())