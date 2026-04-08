# %% 코딩 예제 06-08unpacking.py
# 상품 목록과 각 상품의 가격을 입력 받음
def get_purchase():
    products = input("구매한 상품 목록 (콤마로 구분): ").split(',')
    prices = input("각 상품의 가격 (콤마로 구분): ").split(',')
    return products, prices

# 여러 정수 형태 문자열을 변환해 정수의 목록을 반환
def convert_int(*args): # 언패킹해서 args의 요소들을 전달
    lst=[]
    for i in args:
        lst.append(int(i))
    return lst

# 총 금액 계산
def calculate_total(*prices):
    total = sum(prices)
    return total

# 사용자로부터 상품 목록과 가격을 입력받음
products, prices = get_purchase()
# 입력된 가격을 정수로 변환하고 언패킹하여 총 금액 계산
prices = convert_int(*prices)
# 다음 한 줄의 컴프리헨션으로도 가능 
# prices = [int(price) for price in prices]

total_price = calculate_total(*prices)

# 결과 출력
print("\n상품 목록:", products)
print("가격 목록:", prices)
print("총 금액:", total_price, "원")
