#count() : 튜플에서 특정 값이 몇 번 등장했는지 세어줘.
my_tuple = (1, 2, 3, 2, 2, 4)
count_of_2 = my_tuple.count(2)
print(count_of_2)  # 출력: 3 (2가 3번 등장)

#index() : 튜플에서 특정 값이 **처음 등장하는 위치(인덱스)**를 찾아줘.
my_tuple2 = (10, 20, 30, 20, 40)
index_of_20 = my_tuple2.index(20)
print(index_of_20)  # 출력: 1 (20이 처음 나타난 위치)

#튜플 길이 구하기: len()
my_tuple3 = (1, 2, 3, 4)
print(len(my_tuple3))  # 출력: 4

#요소 포함 여부 확인: in
my_tuple4 = (1, 2, 3)
print(2 in my_tuple4)  # 출력: True

#튜플 병합: + 연산자
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # 출력: (1, 2, 3, 4)

#튜플 반복: * 연산자
my_tuple = (1, 2)
print(my_tuple * 3)  # 출력: (1, 2, 1, 2, 1, 2)


#튜플의 데이터 교환
a = 10 #변수
b = 20 #변수
print(f"교환 전 : a:{a}, b:{b}")
a,b = b,a #변수 값을 기반으로 튜플을 만들었음 소괄호가 없어도 콤마가 있다면 튜플로 간주
print(f"교환 후 : a:{a}, b:{b}")
#이렇게 값을 변경하지는 못하지만 가지고 있는 값을 가지고 교환이 가능하다.


'''
# 리스트와 튜플 데이터 교환
#튜플을 리스트로 변환하거나, 리스트를 튜플로 변환해서 데이터 교환을 수행할 수도 있다
my_list = [10, 20, 30] #리스트
tuple10 = (40, 50, 60) #튜플

# 튜플과 리스트 간의 교환
my_list[0], tuple10 = tuple10, my_list[0]
#my_list[0] : 리스트의 첫 번째 요소 (10)
#tuple10은 (40, 50, 60)라는 튜플 자체를 나타낸다.
#my_tuple과 my_list[0]의 값이 (my_tuple, my_list[0]) 형태의 튜플로 묶임

print(my_list)  # 출력: [(40, 50, 60), 20, 30]
print(tuple10)  # 출력: 10
'''



