ft = filter(lambda x :x%2 == 0 , range(1,11))
list(ft)

#실습문제 1 : [ -10, 1, 4, 6, 8, 10 ]를 nums 리스트에 저장하고 양수만 추출하는 필터함수를 만들어 출력하시오 

nums = [-10, 1, 4, 6, 8, 10]
ft = filter(lambda x : x > 0, nums)
list(ft)

#실습문제 2 :langs = ['java', 'python', 'c/c++', 'kotlin'] 에서 길이가 5이상인 내용만 필터하시오

langs = ['java', 'python', 'c/c++', 'kotlin']
list(filter(lambda x : len(x) >= 5, langs))

#filter 함수에서 첫번째 인자가 None 이면 두번째 리스트에서 참 값만 추출
random_list = [1, 'a', 0, '', False, True, '0', 3.4]
list(filter(None, random_list))

#문자에서 모음만 추출하는 필터함수
latters = list('python java')

#문자가 모음이면 True 반환
def filter_vowels(latters) :
  vowels = ['a', 'e', 'o', 'i', 'u']
  return latters in vowels

list(filter(filter_vowels, latters))

#filter 함수 응용예제
#회원명단
users = [{ 'email' : 'aaa@naver.com', 'name' : '이현식', 'gender' : 'M'},
        { 'email' : 'bbb@naver.com', 'name' : '강바람', 'gender' : 'M'},
        { 'email' : 'ccc@naver.com', 'name' : '들국화', 'gender' : 'M'},
        { 'email' : 'ddd@naver.com', 'name' : '소나무', 'gender' : 'F'},
        { 'email' : 'eee@naver.com', 'name' : '채송화', 'gender' : 'F'} ]

def is_men(user) :
  return user['gender'] == 'M'

def is_women(user) :
  return user['gender'] == 'F'

list(filter(is_men, users))
list(filter(is_women, users))