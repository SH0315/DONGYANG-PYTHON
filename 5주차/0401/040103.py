# 가변인자 (같은 함수 호출시에 매개변수의 갯수가 다를 경우)

#가변인자 사용 X
def profile(name, year, subject1, subject2, subject3, subject4, subject5) :
    print(f"이름 : {name}\t 학년 : {year}학년\t", end = " ") # end = " " -> 줄바꿈 방지
    print(subject1, subject2, subject3, subject4, subject5)
    
    
profile("강바람",2,"Pythom", "JAVA", "C++", "C", "C#")
profile("들국화",1,"HTML", "Kotlin", "", "", "")

#가변인자 사용 O
def profile(name, year, *subject) :
    print(f"이름 : {name}\t 학년 : {year}학년\t", end = " ") # end = " " -> 줄바꿈 방지
    for sub in subject :
        print(sub, end = " ")
    print()   

profile("강바람",2,"Pythom", "JAVA", "C++", "C", "C#")
profile("들국화",1,"HTML", "Kotlin")

#교재 282~283
def sum_numbers(*args) :
    result = 0
    for num in args :
        result += num
    return result

total = sum_numbers(1,2,3,4,5,6,7,8,9,10)
print("합계:", total)

#리스트나 투플은 불가능함 