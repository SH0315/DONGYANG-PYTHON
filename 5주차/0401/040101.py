# 함수 : 명령어(프로그램)의 일부, 기능을 수행하는 단위
# 1) 매개변수, 리턴값
# 2? 함수정의, 호출

# 1) 매개변수 X / return 값 X
#함수 정의
def greeting () :
    for i in range(1,6) :
        print("안녕")
        
#함수 호출
greeting()


# 2) 매개변수 O / return 값 X
def greeting (lang,cnt) :
    for i in range(cnt) :
        print(lang)
        
greeting("안녕", 5)
greeting("Hello", 10)


# 3) 매개변수 X / return 값 O
def sum_1_100 () :
    sum = 0
    for i in range(1, 101, 1) :
        sum = sum + i
        
    return sum
    
        
print(f"1~100까지의 합은 {sum_1_100()}입니다.")


# 4) 매개변수 O / return 값 O
def sum_to(start, end) :
    sum = 0
    for i in range(start, end + 1, 1):
        sum = sum + i
    
    return sum

print(f"1~10000까지의 합은 {sum_to(1,10000)}입니다.")
