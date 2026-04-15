points = [100, 200, 300, 400, 500]
print(points)


# 리스트에 있는 값 10씩 더하는 예제
point_add = []
for i in points:
    point_add.append(i + 10)
print(point_add)

# 위 예제를 짧게 표현
point_add = { i + 10 for i in points}
print(point_add)

#다음 subject에 있는 요소의 길이를 갖는 subject_len을 한줄로 코당하여 만들어 출력하시오
subject = ['basic', 'kotlin', 'java', 'python', 'C', 'C++']
print(subject)

#subject에 있는 요소들의 길이를 출력
subject_len = [len(i) for i in subject]
print(subject_len)

# subject에 있는 요소를 모두 대문자로 출력
subject_upper = [i.upper() for i in subject]
print(subject_upper)