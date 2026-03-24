#변수를 이용한 응용
#print("우리집 강아지는 두부에요 ")
#print("두부는 3살이고, 산책을 좋아해요")
#print("두부는 어른(3살이상)일까요? True")

#위의 출력내용에서 강아지 두부 3 산책 True를 변수에 저장한 후
#변수값을 이용하여 출력하새요

pet = "강아지"  
name = "두부" 
age = 3
play = "산책"
adult = (age >= 3)


print("우리집 " + pet + "는 " + name + "에요")
print(name + "는 " + str(age) + "살이고, " + play + "을 좋아해요")
print(name + "는 " + "어른(3살이상)일까요? " + str(adult) )


