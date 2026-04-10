#IF문
temp = 34
if temp >= 34 :
    print("폭염 주의하십시오")
else :
    print(f"기온은 {temp}도 입니다.")
    

#if else if
age = 10
if age > 70 :
    print("노인")
elif age >= 20 :
    print("성인")
else :
    print("미성년자")
    
#문제 기온이 어때요?
temp = int(input("오늘 기온이 어때요?: "))
if temp >= 30 :
    print("너무 더워요")
elif 10 <= temp < 30  :
    print("괜찮은 날씨에요")
elif temp < 10 :
    print("외투를 챙기세요") 
else :
    print("너무 추워요")


#리스트와 다중조건 판단
pocket = ["paper", "cellphone"]
card = True
if ("money" in pocket) or "card" :
    print("택시를 타고 가세요")
else :
    print("걸어가세요")

# 리스트와 다중조건 판단 에제를 조건부 표현법으로 나타냄
print("택시 타고 가세요" if "money" in pocket or card else "걸어가세요")  
   
#조건부 표현법     
#(조건문이 참일때) if(조건문) else (조건문이 거짓인 경우)
score = int(input("점수는 몇점?: "))
print("Success" if score >= 60 else "Failure")



