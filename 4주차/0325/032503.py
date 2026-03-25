# 표준 압력 두수 비교
# 두수 입력 받기

num1 = float(input("첫번째 수를 입력하세요: "))
num2 = float(input("두번째 수를 입력하세요: "))

result = num1 if num1 > num2 else  num2 
print(f"두 수중에 큰 수는 {result} 입니다.")