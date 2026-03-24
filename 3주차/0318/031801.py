# 리스트: 배열과 같이 여러변수를 한번에 선언하고 사용
str1 ="강바람"
list1 = ["강바람"]

print("문자열: " + str1 )
 #  print("리스트: " + list1)  일반적인 출력법으로는 에러발생 (리스트는 문자열 취급 X)
print("리스트: " + str(list1))

#친구들 이름을 리스트에 넣고 여러 함수 사용
friends = ["강바람", "들국화", "민들레"]
print("최초의 친구들: " , friends)


# 리스트 안에서 몇번 인덱스인지
print("들국화의 위치: ", friends.index("들국화"))


# 리스트에 추가
friends.append("소나무")
print(friends)


#인덱스와 인덱스 사이에 추가
friends.insert(1,"민들레")
print(friends)


#리스트 안 인덱스 삭제 (맨 뒤에 삭제됨)
friends.pop()
print(friends) 

friends.remove("민들레")
print(friends)


#리스트 안에 있는 내용 출력
print(friends[0])
friends[0]


# 퀴즈1 강바람 몇명인지? 
friends.append("강바람")
print("강바람은 몇 명?:",friends.count('강바람'))
friends[0] = '강바람1'
friends[3] = '강바람2'
print('또다른 강바람: ' , friends)


#"들국화"가 있는가?
print("들국화" in friends)  #TRUE
print("소나무" in friends) #FALSE


if  "들국화" in friends:
        print("들극화가 있습니다")
else :
        print("들국화가 없습니다")
        

if  "들국화" in friends:
        print("들극화가 " , (friends.index("들국화") + 1) , "번째에 있습니다.")
else :
        print("들국화가 없습니다")
        

#이름 정렬하기
friends.sort()
print("정렬 후의 리스트: ", friends)


#순서 반대로 정렬하기
friends.reverse()
print("반대로 정렬한 리스트: ", friends)


#모두 지우기
friends.clear()
print("모두 지운 리스트:", friends)


#빈 리스트인지 확인하기
if not friends:
    print("친구없음")
