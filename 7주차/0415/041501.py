print('python'[0])  # p
print((1,2,3), type((1,2,3)))   # (1,2,3)
a = (1,2,3)
print(a, type(a))               #(1, 2, 3) <class 'tuple'>
print(list(a), type(list(a)))   #[1, 2, 3] <class 'list'>

b = (1,1,2,3,3,1,6)
print(b, type(b))

# 위의 예시에서 중복을 제외해서 출력하여라 (type 변경)
# set 으로 자료형을 변경하면 중복값을 지울 수 있음 (집합이라 중복 X)
print(set(b), type(set(b)))

