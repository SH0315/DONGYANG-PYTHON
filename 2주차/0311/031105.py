# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하세요

# 예) http://naver.com
# 규칙1: http:// 부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 나는 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#               (nav)                (5)             (1)        (!)
# 예) 생성된 비밀번호 : nav51!


url = "https://naver.com"
# 규칙1 -> url에 저장된 문자열 중 https:// 를 ""(공백) 으로 변환해서 저장
rule1 = url.replace("https://","") 

# 규칙2 -> naver.com 의 첫자리부터 .부분 전까지를 rule2에 저장
rule2 = rule1[0:rule1.index(".")] 

#규칙3 -> nav : naver에서 첫자리부터 e부분 전까지 
#           5 : len(rule2) 로 글자 갯수를 구함
#           1 : rule2.count('e')로 e의 갯수를 구함
# 구한 값을 출력을 위해 str() 로 감싸서 문자열로 형변환      
rule3 = rule2[0:rule2.index('e')] + str(len(rule2)) + str(rule2.count('e')) + "!" 

# 출력할때는 f태그와 함수를 사용해서 출력
print(f"생성된 비밀번호는 {rule3} 입니다")


