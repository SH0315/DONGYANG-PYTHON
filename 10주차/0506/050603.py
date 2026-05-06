# #여러 값을 콤마(,) 구분시켜 리스트에 저장
lst = []
i = 1
while True :
    s = input(f'{i}번 학생이 좋아하는 과목들을 입력하세요 또는 종료 : ' )
    if s == '종료' :
        break
    else :
        lst = []
        lst.append(s.split(','))
        i = i + 1
        print(lst)  
        
# langs는 빈 딕셔너리로 초기화하고 사용자로 부터 사용가능한 언어를
# C, JAVA, PYTHON, HTML 입력받아 (단, 복수 개 입력시 , 로 구분)
# 종료 입력시, 무한반복을 종료한 후 langs 딕셔너리 내용을 출력하시오

langs = {}
while True :
    s = input('사용가능한 언어 또는 종료 : ')
    s = s.lower() # 대문자로 입력해도 소문자로 통일
    if s == '종료' :
        print('프로그램을 종료합니다')
        break 
    
    for a in s.split(',') :
        # 딕셔너리 안에 이미 존재하는 안어인 경우
        if a in langs :
            langs[a] += 1
        # 딕셔너리 안에 없는 새로운 언어인 경우
        else :   
            langs[a] = 1

for key, value in langs.items():
    print(f'수강한 언어{key} : {value}번')
            