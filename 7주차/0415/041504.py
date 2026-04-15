#항목의 논리를 검사하는 함수 all() , any()

#all은 
# 이터러블의 모든 항목이 참이면 TRUE
# 모두 비어있으면 True
a = all([3, 7>=4, 'py' in 'python', 3%2])
print(a)

print(f"all(''), {(all(''))}")
print(f"all([]), {(all([]))}")
print(f"all(()), {(all(()))}")

print(f"all(['']), {(all(['']))}") # FALSE


#any는 
#이터러블의 하나리도 항목이 참이면 TRUE 
#모두 비어있으면 FALSE
print(f"any(''), {(any(''))}")
print(f"any([]), {(any([]))}")
print(f"any(()), {(any(()))}")

print(f"any(['a']), {(any(['a']))}") # TRUE

