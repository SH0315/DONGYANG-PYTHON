# 문제 1) 두 변수의 사칙 연산 결과를 출력하는 프로그램을 함수를 이용해서 구현하시오

# def add (num1, num2) :
#     return num1 + num2

# def sub (num1, num2) :
#     return num1 - num2

# def mul (num1, num2) :
#     return num1 *  num2

# def div (num1, num2) :
#     if num2 != 0 :
#         return num1 / num2

# num1 = float(input("첫번쨰 수를 입력하시오 : "))
# num2 = float(input("두번쨰 수를 입력하시오 : "))

# print(f"입력 받은 두 수의 합은 {add(num1,num2)}입니다.")
# print(f"입력 받은 두 수의 차는 {sub(num1,num2)}입니다.")
# print(f"입력 받은 두 수의 곱은 {mul(num1,num2)}입니다.")
# print(f"입력 받은 두 수의 몫은 {div(num1,num2)}입니다.")

# 문제 2) 계좌계설, 입금, 출하는 함수 만들기

def open_account () :
    print("새로운 계좌가 생성되었습니다.")

    
def depositing(balance, deposit) :
    print(f"입금이 완료되었습니다. 잔고는 {balance + deposit}원 입니다.")
    
def withdraw(balance, deposit) :
    if balance > deposit :
        print(f"출금이 완료되었습니다. 잔고는 {balance - deposit}원 입니다.")
    else  :
        print(f"잔액이 부족합니다. 잔고는 {balance}원 입니다.")
    
    

open_account()    
balance = int(input("잔고를 입력하세요:"))
deposit = int(input("입금 및 출금액을 입력하세요"))


depositing(balance,deposit)
withdraw(balance,deposit)



