'''
try:
    예외가 발생할 수 있는 코드블록
except 발생예외1 as 변수1:
    발생예외1에 해당ㅎ하면 수행되는 코드 블록
except 발생예외2 as 변수2:
    발생예외2에 해당ㅎ하면 수행되는 코드 블록

이렇게 as키워드와 변수 이름을 작성하면 예외객체가 해당 변수에 저장된다.
변수를 추가해보도록 하겠습니다~
'''

try:
    num1 = int(input("첫 번째 정수를 입력하세요 : "))
    num2 = int(input("두 번째 정수를 입력하세요 : "))
    print(f"{num1}나누기 {num2}의 결과는 {num1/num2} 입니다.")
except ArithmeticError as e:
    print(f"산술연산예외 발생!! 상세메시지는 {e}입니다.")

