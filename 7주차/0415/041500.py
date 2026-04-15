#주문 정보를 저정하는 사전데이터 함수를 이용해서 출력

#지원 정보를 저정하는 사전
applys = [] #전역변수

# 지원을 추가하는 함수 생성
def add_applys(name, age,  *dept, **license) :
    global applys #전역변수 사용 및 수정
    apply = { "name" : name, "age" : age, "dept" : dept, "license" : license}
    #리스트 applys 에 딕셔너리 apply를 추가함
    applys.append(apply)

def display_applys() :
    global applys   
    #리스트 applys의 인덱스를 1부터 시작
    for index, apply in enumerate(applys, 1) :
        print(f"지원번호 {index}:")
        print(f"이름 : {apply['name']}")
        print(f"나이 : {apply['age']}")
        
        if apply['dept'] :
            #투플인 dept의  각 요소를 쉼표와 공백을 하나의 문자로 합쳐줌
            print("학과 : " + "," .join(apply['dept']))
        
        if apply['license']:
            print("자격증")
            for key, value in apply['license'].items() :
                print(f"- {key} : {value}")
        print("\n")
        
    
#지원 추가
add_applys("강바람", "25","컴퓨터소프트웨어학과", "AI학과", 토익 = 450, 정보처리 = "기사")
add_applys("이하늘", "26", "게임학과",  정보처리 = "기사", 중등교원 = "2급")
add_applys("들국화", "27", "경영학과", "AI학과", 컴퓨터활용능력 ="1급")
    
 #지원자 출력
display_applys()
    
    
    