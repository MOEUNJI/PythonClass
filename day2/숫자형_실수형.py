height = 160.5
weight = 45.6

print(height)
print(weight)
#이렇게 실수를 출력할 수 있다

#실수도 정수와 마찬가지로 연산이 가능하다
print(height - weight) #114.9 나올것


#만약 소수점이 딱 떨어지는 숫자를 연산한다면?
x = 2.2
y = 2.8
print(x + y) # 5.0이 출력될것
#실수와 실수의 연산은 소수점 이하의 값까지 연산하기 때문에
#5.0 이라는 실수 형태로 나타난다.


#실수와 정수의 연산도 가능할까?
first = 3.9
second = 3
print(first * second) # 11.7 나올것 ( 가능하다 )


#두 숫자 모두 정수이지만 소수점을 포함한다면?
seven = 7.0
three = 3.0
print(seven + three) # 10.0 출력
#소수점.0을 포함한 숫자는 실수로 간주된다.
# 우리 눈에는 정수로 보여도 코드에서는 실수로 연산한다.


#정수를 실수로 반환하려면?
print(float(1)) # 1.0
print(float(True)) # 1.0
print(float(False)) # 0.0
print(float('3.14')) # 문자열 3.14를 3.14실수형으로 변환
print(float('100')) # 문자열 100을  100.0으로 변환
