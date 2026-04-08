#주문 정보를 저정하는 사전데이터 함수를 이용해서 출력

#주문 정보를 저정하는 사전
orders = [] #전역변수

# 주무을 추가하는 함수 생성
def add_orders(item,  *options, **special_requests) :
    global orders #전역변수 사용 및 수정
    order = { "item" : item, "options" : options, "special_requests" : special_requests}
    #리스트 orders 에 딕셔너리 order를 추가함
    orders.append(order)

def display_orders() :
    global orders   
    #리스트 orders의 인덱스를 1부터 시작
    for index, order in enumerate(orders, 1) :
        print(f"주문 {index}")
        print(f"항목 : {order['item']}")
        if order['options'] :
            #투플인 options의  각 요소를 쉼표와 공백을 하나의 문자로 합쳐줌
            print("옵션 : " + "," .join(order['options']))
        if order['special_requests']:
            print("특별요청")
            for key, value in order['special_requests'].items() :
                print(f"- {key} : {value}")
        print("\n")
        
    
#주문 추가
add_orders("피자", "치즈", "페퍼로니", 소스 = "바베큐", 요구사항 = "양파빼고")
    
 #주문 출력
print("주문 목록")
display_orders()
    
    
    