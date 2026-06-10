import os
print(os.name)
print(os.getcwd()) # 실행 폴더 위치
print(os.listdir()) # 실행 폴더 하위의 폴더와 파일리스트

# 파일 생성하고 내용저장  + 파일이름 변경
#with open("original.txt", "w") as file :
    #file.write("Test2")  
    
#파일명 변경
#os.rename("original.txt", "new.txt")

#파일 제거
#os.remove("new.txt")

#시스템 명령어 실행
os.system("dir")