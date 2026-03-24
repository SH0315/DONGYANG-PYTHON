# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하세요

# 예) http://google.com
# 규칙1: http:// 부분은 제외 => google.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 나는 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'g' 갯수 + "!" 로 구성
#               (goo)                (6)             (2)        (!)
# 예) 생성된 비밀번호 : goo62!

site = "http://google.com"

site1 = (site[7:]) # google.com

site2 = (site1[:6])

site3 = (site2[:3] + str(len(site2)) + str(site2.count('g')) + "!"  )
site3 = (site2[:3] + str(len(site2)) + str(site2.count('g')) + "!"  )

print(f"생성된 비밀번호는 {site3}입니다")


name = "상혁"
age = 20
score = 87.456

print(f"이름:  {name} | 나이:   {age}세 |  점수:  {score:.2f}점")