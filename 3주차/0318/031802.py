# 리스트는 여러 타입의 요소를 가질 수 있음
list1 = [2, "1", 3, 4, 5, True ]
list2 = [6,7,8,"9", "10", 5.5, [1,2,3,4,5]]

#리스트 확장
print(list1 +list2)
print(list1[0])
print(list2[6]) # 결과 [1,2,3,4,5]
print(list2[6][2]) # 결과 3 (리스트 안에 있는 리스트에 있는 수를 가져옴)

#리스트 확장2
list1.extend(list2)
print(list1)