#ZIP 함수
keys = ['강바람', '민들레', '들국화']
scores = [90, 75, 85]

my_dict = dict(zip(keys, scores))
print(my_dict, type(my_dict))

#딕셔너리 컴프리헨션
#반복문과 조건문을 활용하여 한 줄로 간결한 딕셔너리를 새로 만드는 방법
# {key: value for 변수 in 반복가능한것} 의 형태

#score에서 80점 이상인 키 : 값 의 쌍을 PASSED에 저장
scores = {'강바람' : 90, '민들레' : 75, '들국화' : 85}
passed = {name : score for name, score in scores.items() if score >= 80 }
print(passed)

#문제
data = {'data1' : "파이썬 데이터 분석" ,
        'data2': "자바스크립트 프로그래밍",
        'data3' : "파이썬 웹 개발"
        }

#파이썬이 포함된  값을 추춣여 python_data 딕셔너리에 저장하고 출력
python_data = { type : name for type, name in data.items() if "파이썬" in name }
print(python_data)