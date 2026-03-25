#프로그래밍 언어와 개발연도를 튜플()을 요소로해서 리스트[]로 구성

p1= [ ('basic', 1964), ('java', 1995), ('kotlin', 2016), ('python', 1991), ('c', 1973)]

print(p1,type(p1))
print(sorted(p1))

print(sorted(p1,key = lambda lang: lang[0])) # 이름 순 정렬

print(sorted(p1,key = lambda lang: lang[1])) # 연도 순 정렬

print(sorted(p1, key = lambda lang : len(lang[0]))) # 이름길이 순 정렬

# p1를 딕셔너리로 변경한후 이름 순 정렬
p1_dict = dict(p1) # p1 딕셔너리 화
sorted_dict = dict(sorted(p1_dict.items())) # p1의 요소들을 이름 순 정렬
print(sorted_dict) 