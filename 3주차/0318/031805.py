#튜플(tuple) : 리스트랑 같지만 읽기 전용
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#튜플 사용하기 좋은 예
a = 10 
b = 20
print("변경 전:" ,a , b)
a, b = b , a # 값 변경
print("변경 후:", a , b)


#튜플 사용하기 좋은 예2
name, no, dept = ("임상혁", 20232324, "컴퓨터공학")
print(name, no, dept)

student_record = ("임상혁", 20232324, "컴퓨터공학")
print(student_record[0], student_record[1], student_record[2])
