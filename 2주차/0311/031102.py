#문자열슬라이싱(중간고사 출제)
jumin = "990107-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2직전까지 (2미만)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 :  " + jumin [:6]) # : 앞에 수를 넣지 않으면 처음부터 시작
print("번호후반 : " + jumin[7:14])
print("번호후반 : " + jumin[7:])
print("번호후반 : " + jumin[-7:]) # 맨뒤의 인덱스는 음수인 경우 -1부터 시작
print("번호후반 : " + jumin[-7])