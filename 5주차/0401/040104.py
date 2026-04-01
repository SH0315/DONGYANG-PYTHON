#전역변수 & 지역번수 (함수의 유효범위 : 학생회장, 반대표)

gun = 10
#방식 1)
def check () :
    print(f"[함수 내] 남은 총 : {gun}")

def checkpoint1(soldiers) :
    
    global gun  # 전역변수를 수정하려면 global를 사용해서 함수안에서 수정
    gun = gun - soldiers
    #gun = 10  ->  함수안에서 선언하면 지역변수
    
    print("[함수 내] 남은 총 : {0}".format(gun))
    

    
check()
checkpoint1(2)

print("-"*22)

#방식 2)
gun = 10

def checkpoint1(gun, soldiers) :         # 지역변수로 변환 (복사본을 사용함)
    gun = gun - soldiers                 # 전역변수를 가져와 값을 복사해서 지역변수로서 사용
    print(f"[함수 내] 남은 총 : {gun}")
    

    
print(f"[함수 내] 전체 총 : {gun}")       # 10
checkpoint1(gun, 2)            # 8

# CASE 3) 함수 안에서 전역변수를 읽기만 한다면?
def addone() :
    print("전역변수 : i", i)
    
i = 20
print("호출전 i = ", i)
addone()
print("호출후 i = ", i)
# 함수 안에서 정의나 수정하지 않아서 전역변수로 그대로 인식함

#CASE 4
#CASE 3에서 값을 변경해서 출력하려면?
def addone(ii) :
    return(ii+1)

i = 20
print("호출전 i = ", i)
i = addone(i)
print("호출후 i = ", i)
    





    
    
    
