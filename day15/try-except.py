'''
try:
    예외가 발생할 수 있는 코드
    문제가 생길 수도 있으니, 여기서 조심해서 실행해!"라고 말하는 느낌이에요.
except:
    예외가 발생했을 때 수행되는 코드
    문제가 생겼네! 그러면 이렇게 해결하자!"라는 느낌이에요.

만약 try에서 예외가 발생하면 해당 예외는 자동으로 except블록으로 전달됨
except블록에는 예외가 발생했을 때 실행할 코드를 작성해놓음
만약 에러가 발생하지 않았다면? except는 실행되지 않음
'''

# try:
#     num1 = int(input("첫 번째 정수를 입력하세요 : "))
#     num2 = int(input("두 번째 정수를 입력하세요 : "))
#     print(f"{num1} 나누기 {num2}는 {num1 / num2}입니다. ")
#
# except:
#     print("예외가 발생했습니다!")


try:
    num1 = int(input("첫 번째 정수를 입력하세요 : "))
    num2 = int(input("두 번째 정수를 입력하세요 : "))
    print(f"{num1} 나누기 {num2}는 {num1 / num2}입니다. ")
except ArithmeticError:
    print("산술연산 예외가 발생했습니다.")
except ValueError:
    print("입력값 예외가 발생했습니다.")