#enumerate(iterable, start=0)  
#점자(index)룰 자동으로 만들어 첨자와 값의 쌍인 투플로 만들어 주는 내장함수
#호충 결과는 enumerate 객체 (주소)
p1 = ['python', 'C', 'java']
print(list(enumerate(p1)))
print(list(enumerate(p1, start=1)))

lst = 'python'
print(list(enumerate(lst)))

seasons = ("Spring", "Summer", "Fall", "Winter")
for i, season in enumerate(seasons, start=1) :
    print(f'{i} : {season}')
    
print("ㅡ" * 20)

for season in enumerate(seasons, start=1) :
    print(f'{season[0]} : {season[1]}')