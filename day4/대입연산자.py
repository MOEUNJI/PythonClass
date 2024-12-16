num1 = 100 # num1 이라는 변수에 100이라는 값을 넣어줌
num2 = 55 # num2라는 변수에 55라는 값을 할당함
# 변수 오른쪽에 값은 단순히 하나의 숫자데이터를 삽입할 뿐만 아니라,
# 오른쪽 연산의 결과를 저장하기도 함

num1 = num1 - 20 # num1의 값에서 20을 뺀 새로운 값을 할당
print(num1) # 80 나올것

# 자 그럼 num2를 100으로 만들어 주세요~
num2 = num2 + 45
print(num2)


'''
복합대입연산자 종류
1. a += b ( a = a + b )
2. a -= b ( a = a - b )
3. a *= b ( a = a * b )
4. a /= b ( a = a / b )
5. a //= b ( a = a // b )
6. a %= b ( a = a % b )
'''

#복합대입연산자
number = 4

number += 1 #number = number + 1 이렇게 작성한 거랑 똑같음
print(number) # 5 출력될것

number = number + 1
print(number) # 6출력될것

# 대입연산자를 통해 number를 100을 만들어보세요
number += 94
print(number)

seven = 7
three = 3

ten = seven + three

seven += three # 7+3
print(seven) # 10 나올것

ten -= seven # 10-10
print(ten) # 0 나올것

three *= seven # 3 * 10
print(three) #30 나올것

three /= seven # 30 / 10
print(three) # 3.0
# 소수점이 나오는 이유는 파이썬에서는 나눗셈을 사용하면 부동소수점타입으로 출력함
# float 타입이라고 생각하면 됨! 나눗셈의 결과가 딱 떨어지더라고 .0이 붙음
# 정수나눗셈을 원한다면 몫만 출력하는 //= 를 사용해야함

five = 5
two = 2

five //= two # 5를 2로 나눈 몫을 출력
print(five) # 2가 출력될것

two **= five # 2 의 2제곱
print(two) # 4가 출력될것

two += 1 # 나머지연산을 위해 홀수로 만들려고 1을 더함
print(two) #5 가 출력될것

two %= five # 5를 2로 나눈 나머지
print(two) # 1이 출력될것


