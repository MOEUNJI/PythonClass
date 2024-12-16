'''
변수명 = (요소1,요소2,요소3)
'''
from sys import orig_argv

#자료형
alphabets = ('a','b','c') #문자
bools = (True,True,True) #불리언값
greetings = ("안녕하세요","튜플 배우는 중!","입니다.") # 문자열

#튜플만들기
my_tuple = (1,2,3) #소괄호로 생성
single_tuple = (5,) #요소가 1개일때는 반드시 콤마 붙이기!
another_tuple = 10,20,30 #소괄호 없이도 가능

#튜플의 특징
# 1. 변경 불가능 : 값을 추가하거나 삭제 불가능
# 2. 인덱스로 접근이 가능하다 : 리스트와 똑같음
# 3. 중첩 가능: 튜플 안에 다른 튜플이나 리스트를 넣을 수도 있다

#변경시도
# my_tuple[0] = 10  # 오류 발생!

#인덱스로 튜플 출력
print(my_tuple[1]) #2
print(alphabets) #('a', 'b', 'c')

#음수 인덱스로 튜플 출력
print(another_tuple[-3]) #오른쪽부터 출발 10

#중첩
multi_tuple = (1,(2,3),[4,5]) #튜플 안에 2,3 튜플 있고, 4,5 리스트 있음
print(multi_tuple[2]) #[4, 5]
print(multi_tuple[1][1]) #3

#튜플 슬라이싱
slice_tuple = (3,10,"파이썬",True,"치킨",23)
print(slice_tuple[1:4]) #(10, '파이썬', True) 마지막 인덱스 빼고 출력
print(slice_tuple[0:5]) #(3, 10, '파이썬', True, '치킨')

