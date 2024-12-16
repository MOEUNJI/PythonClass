'''
try:
    예외가 발생할 수 있는 코드 블록
except:
    예외가 발생했을 때 수행되는 코드 블록
else:
    정상적으로 실행되면 수행되는 코드 블록

'''

try:
    number = int(input("좋아하는 숫자를 입력해주세요"))
except ValueError as e: # 문자열을 정수로 변환할 수 없을 때 예외 발생
    print(e) # 예외 출력하여 원인을 아렬줌
else: # try 블록에서 예외가 발생하지 않고 정상 실행되었을 때 실행하는 코드
    if number % 2 == 0:
        print("짝수를 좋아하시는군요")
    elif number < 0:
        print("음수를 좋아하시는군요")
    else:
        print("홀수를 좋아하시는군요")