'''
변수명  = {요소1,요소2,요소3}

set(세트로 바꾸고 싶은 다른 자료형)
'''
from traceback import print_tb

str = "apple"
list1 = [1,2,3]
tuple1 = (1,2,3)

print("<각자의 형태를 가진 자료형들>")
print("str : ",str)
print("list1 : ",list1)
print("tuple1 : ",tuple1)

#set로 변환
set_str = set(str)
set_list = set(list1)
set_tuple = set(tuple1)

print()

#set로 변환된 값 출력
print("<set로 변환한 자료형들>")
print("set_str : ",set_str)
print("set_list : ",set_list)
print("set_tuple : ",set_tuple)


#요소에 접근하기 위해 리스트,튜플로 변환하기
str_banana = "banana" # 바나나 생성
set_banana = set(str_banana) #바나나를 세트로 변환
print(set_banana) #세트 출력해보면 n,a,b만 남은것을 볼 수 있음(중복제거)

list_banana = list(set_banana) #세트바나나를 리스트로 변환
tuple_banana = tuple(set_banana) #세트바나나를 튜플로 변환

print(list_banana) #['n', 'b', 'a']
print(tuple_banana[1]) #('n', 'b', 'a')

#마구잡이 알파벳에서 중복을 삭제하고 오름차순정렬
#1. 중복 삭제
str_random = "avwheflanvfasjcdsfewmbnjkln" #마구잡이 알파벳 생성
str_random = set(str_random) #중복제거
print(str_random)

#리스트로 변환
list_str = list(str_random)
print(list_str) # [] 대괄호로 변경 되었나 확인하기

#리스트를 오름차순으로 변경
list_str.sort()
print(list_str)

#특정 순서의 알파벳 출력
print(f"3번째로 작은 알파벳은 {list_str[2]} 입니다")
print(f"7번째로 작은 알파벳은 {list_str[6]} 입니다")
