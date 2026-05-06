#자주 사용하는 파이선 코딩
#딕셔너리로 혈액형별 인원수를 카운트하는 프로그램
# 1. blood 딕셔너리로 'A' , 'B', 'O', 'AB' 를 키로 해서 각 값을 0으로 초기화한다.
blood = {'A' : 0 , 'B' : 0 , 'O' : 0 , 'AB' : 0}
# 2. 무한반복하면서 사용자로부터 혈액형을 입력받아 각각의 키에 해당하는 값을 증가시킨다
while True:
    s = input("혈액형을 입력하거나 종료 : ")

    if s == "종료":
        print("프로그램을 종료합니다")
        break

    elif s in blood:   # 정확히 키에 있는 값인지 확인
        blood[s] += 1  # 해당 혈액형 카운트 증가
    else:
        print('잘못 입력했습니다')

# 3. 종료 후 딕셔너리 내용을 출력
for key, value in blood.items() :
    print(f'{key}형 : {value}명 ')