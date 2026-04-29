
#문제1) 다음 두 목록을 딕셔너리로 변환해 출력하는 프로그램을 작성하시오
print('문제1 결과')

keys = ['Ten', 'Twenty','Thirty']
values = [10, 20, 30]
info = dict(zip(keys,values))
print(info)

print("ㅡ" * 20)
#문제2) 다음을 참조해 식료품점의 상품명와 가격을 관리하는 프로그램
print('문제2 결과')

fruits = ['사과', '바나나', '포도', '배']
prices = (1000,500,1200, 1500)
#를 이용해 딕셔너리를 만들고 
#원하는 작업을 선택하시오:
#1. 가격표 출력
#2. 상품 가격 검색
#3. 가격 업데이트
#4. 상품추가
#5. 종료 
#예) 
#1
#상품목록 및 가격:
#사과 : 1000원
####################
#결과
#가격을 업데이트할 상품이름을 입력하시오 : 바나나
#새로운 가격을 입력하시오: 1000
#바나나의 가격이 1000원으로 업데이트 되었습니다. 
print('문제2 결과')

fruits = ['사과', '바나나', '포도', '배']
prices = (1000, 500, 1200, 1500)

# 딕셔너리 생성
menu = dict(zip(fruits, prices))

while True:
    print("\n원하는 작업을 선택하시오:")
    print("1. 가격표 출력")
    print("2. 상품 가격 검색")
    print("3. 가격 업데이트")
    print("4. 상품추가")
    print("5. 종료")

    choice = input("작업 번호 입력: ")

    if choice == '1':
        print("\n상품목록 및 가격:")
        for name, price in menu.items():
            print(f"{name} : {price}원")

    elif choice == '2':
        name = input("가격을 검색할 상품이름을 입력하시오: ")
        if name in menu:
            print(f"{name}의 가격은 {menu[name]}원입니다.")
        else:
            print("해당 상품이 존재하지 않습니다.")

    elif choice == '3':
        name = input("가격을 업데이트할 상품이름을 입력하시오: ")
        if name in menu:
            new_price = int(input("새로운 가격을 입력하시오: "))
            menu[name] = new_price
            print(f"{name}의 가격이 {new_price}원으로 업데이트 되었습니다.")
        else:
            print("해당 상품이 존재하지 않습니다.")

    elif choice == '4':
        name = input("추가할 상품이름을 입력하시오: ")
        if name in menu:
            print("이미 존재하는 상품입니다.")
        else:
            price = int(input("가격을 입력하시오: "))
            menu[name] = price
            print(f"{name}이(가) {price}원으로 추가되었습니다.")

    elif choice == '5':
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 입력입니다. 다시 선택하세요.")
            
            
