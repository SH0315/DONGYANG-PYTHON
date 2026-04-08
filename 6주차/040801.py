# #교재 287~      

#  default 매개변수 (매개변수 값이 전달되지 않으면 기본으로 사용하는값)
#  한번 호출된 리스트 그대로 사용
def default_arg(a, obj = []):
    obj.append(a)
    return obj

# 빈 리스트에 리스트를 넣어주었기 때문에 주어진 리스트에 값을 추가하는 구조
print(default_arg(1, [1,2,3]))

# 빈 리스트에 리스트가 없고 값만 주었기 때문에 새로 만들어진 리스트에 값만 추가되는 구조
print(default_arg(2))
print(default_arg(3))


# 호출 될때마다  빈 리스트 생성
def default_arg(a, obj=None) :
    if obj is  None : 
        obj = []
    obj.append(a)
    return obj

print(default_arg(1, [1,2,3]))
print(default_arg(2))
print(default_arg(3))