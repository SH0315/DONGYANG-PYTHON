# 이터러블 과 이터레이터
# iteralbe 객체 -> 반복 가능한 객체

a = [1,2,3]
a_iter = iter(a)
print(a)
print(type(a))
print(a_iter)
print(type(a_iter))
print(next(a_iter))

b = [1,2,3]
b_iter = iter(b)
print(type(b_iter))
print(b_iter.__next__())

