#피연산자1 if 조건식 else 피연산자2
'''
조건의 결과가 참이면 피연산자 1을 실행하고 거짓이라면 2를 실행한다
이건 피연산자1 조건식 피연산자2 이렇게 3개의 항을 참조하고 있으므로
3항조건연산자라고도 불리는데 c언어, 자바스크립트 하셨던 분들은 사용법이
다른걸 아실거다~
'''

num1 = 100
num2 = 50

big = num1 if num1 > num2 else num2
# 만약 num1이 num2보다 크다면 = True!
# if왼쪽에 있는 값을 big에 대입한다.
print(big)

x = 21
y = 20
if x < y: #x가 y보다 작니? False!
    max = x #조건이 True라면 출력
else:
    max = y #조건이 False라면 출력
print(max) # y의 값 20 출력될것