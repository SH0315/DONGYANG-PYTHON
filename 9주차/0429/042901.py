# ZIP함수
# 조합되는 갯수가 맞아야 하고 맞지 않으면 최소갯수에 맟춰짐
a = ['FTP', 'telnet', 'SMTP', 'DBS' ]
b = (20, 23, 25, 53)

print(zip(a,b))
print(list(zip(a,b)))
#전체적으로 리스트이지만 각 항목은 투플임

print(tuple(zip(a,b)))
#전체적으로 투플이고 각 항목도 투플임

#인자가 3개인 항목을 투플로 구성
print(list(zip('abc',a,b)))

#함수 호출 ZIP() 결과를 iterator이므로 for in문에 사용할 수 없음
for t in zip(a,b) :
    print(f'서비스 :{t[0]} -> 포트 : {(t[1])}')
    
#문제
name = ('강바람', '만들레', '들국화', '채송화',)
age = (20, 22, 21, 22)
score = [90, 89, 68, 77]

for grade in zip(name,age,score) :
    print(f'이름 : {grade[0]}\n 나이 : {grade[1]}\n 점수 : {grade[2]}\n')
    
   