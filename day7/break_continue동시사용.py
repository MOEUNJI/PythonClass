'''
조건
시작 숫자는  0
숫자는 20까지 증가할것인데 조건 2개가 붙는다.
첫번째 조건은 3의 배수는 출력하지 않는다.
두번째 조건은 17전까지만 출력한다.
브레이크와 컨티뉴를 둘 다 사용해서 작성해보기
'''
num = 0
while num < 20:
    num += 1
    if num % 3 == 0:
        continue
    if num == 17:
        break
    print(num,end=" ")

