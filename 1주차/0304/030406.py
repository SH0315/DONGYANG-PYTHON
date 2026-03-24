#변수를 이용한 응용 3) 3개의 역출력 딕셔너리 활용 ( 키 : 값 ) 
import time
station = {"신도림" : 5, "구일" : 4, "개봉" : 3}
# for name, delay in station.items():
#     print(name, delay)

# 역 출력 반복문
for name, delay in station.items(): 
    print("->", end = " ") #줄바꿈 없이 출력
    time.sleep(1)
    print("다음역은 " + name + "입니다.")
     
     # 지연시간 표현 반복문 
    for j in range(delay): #  range의 시작값은 0 -> delay의 값만큼 반복해라
         print("▷ " * (j+1)) 
         time.sleep(1)
    print("이번역은 " + name + "입니다")