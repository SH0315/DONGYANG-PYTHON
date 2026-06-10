# Counter 클래스 : 요소들의 갯수를 세어 딕셔너리 형태로 저장
from collections import Counter
s = "numpy scipy python programming"
counter = Counter(s)

# 문자의 빈도 수 확인 (공백도 하나의 문자로 취급)
count_p = counter['p']
print(f"문자열 'p'의 개수: {count_p}")

# 최다 출현 상위 5개 출력 (most_common 값에 따라 출력할 갯수 달라짐)
for i, item in enumerate(counter.most_common(5)):
    print(f"{i+1}등 {item[0]}: {item[1]} ")
