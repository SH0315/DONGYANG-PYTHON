#집합(set) - 중복안됨, 순서없음
my_set = {1,2,3,4,5}
print(my_set)

#집합을 이용한 수강신청 예제
java = {"임상혁", "태지환", "최진서"}
python = set(["임상혁", "태지환"])

#교집합
print("Java 와 Python 모두 수강" , java & python)
print("Java 와 Python 모두 수강" , java.intersection(python))

#합집합
print("Java 나 Python 수강" , java | python)
print("Java 나 Python 수강" , java.union(python))

#차집합
print("Java 만 듣고 Python 수강 하지 않는 사람" , java - python)
print("Java 만 듣고 Python 수강 하지 않는 사람" , java.difference(python))

#집합에 추가 / 삭제
java.add("김시우")
print(java)

java.remove("김시우")
print(java)