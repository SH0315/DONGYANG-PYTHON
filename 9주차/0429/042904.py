##딕셔너리와 enumerate()로 과일 목록 관리
# 1) 리스트 생성
fruits = ['사과', '바나나', '딸기', "포도"]

# 2) enumerate()을 이용해 인덱스와 함께 목록을 나열
indexed_fruits = enumerate(fruits, start=1)

# 3) 인덱스와 과일을 딕셔너리로 생성
fruits_dict = dict(indexed_fruits)

# 4) 인덱스와 과일을 딕셔너리를 출력하기
for fruit, index in fruits_dict.items() :
    print(f'{index} : {fruit}' )

print("ㅡ" * 20)

# 5) 사용자로부터 선택한 과일의 인덱스 입력받기
choice = int(input("원하는 과일의 인덱스를 입력하세요"))

# 6) 선택한 과일 확인
if choice in fruits_dict :
    selected_fruit = fruits_dict[choice]
    print(f'선택한 과일은 {selected_fruit}')
else :
    print('유효한 인덱스가 아닙니다')
    
print("ㅡ" * 20)
    
# 7) 새로운 과일을 추가
new_fruit = input('새로운 과일을 입력하세요')
next_index = len(fruits_dict) + 1
fruits_dict[next_index] = new_fruit 

# 8) 새로운 과일을 목록(리스트) 에 추가
fruits.append(new_fruit)

# 9) 업데이트된 인덱스와 과일 딕셔너리 출력
print('\n 업데이트된 인덱스와 과일목록')
for index, fruit in fruits_dict.items() :
    print(f'{index} : {fruit}')

print("ㅡ" * 20)

# 10) 업데이트 된 과일 목록 출력
for fruit in fruits :
    print(fruit)

    
     