# 가변 키워드 인자 (값을 딕셔너리로 받음)
def personal_info(**kwargs) :
    for key, value in kwargs.items() :
        #딕셔너리에서 (키 ,값) 을 하나씩 꺼내는 반복문
        print(key, ':', value, sep='')
        # sep 은 추가로 삽입할 문자열 -> 공백이라 아무것도 추가되지 않고 그대로 나옴
        
personal_info(name = '홍길동', age = 20, address = "구로구 동양미래대학교")
personal_info(name = '강바람', no = 1, dept = "컴퓨터 소프트웨어")


 