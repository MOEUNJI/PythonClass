#while 조건식:
    #조건식이 참이면 실행되는 코드

#while 조건식:
    #코드1
    #코드2
    #코드3

count = 0 # 초기값 설정
while count < 3: #조건이 참인지 검사
    print(count) #조건이 참이라면 count 안에 들어있는 숫자를 출력
    count = count + 1 #count안에 들어있는 숫자는 반복문을 돌때마다 1씩 높아져 출력될것
# js나 c언어를 배운 사람들은 count = count + 1 를 count++ 이렇게
#작성하면 되는 거 아니야? 생각하겠지만, 파이썬에는 증감식이 없다
# 사용자 기반이기 때문에 사용자가 보기 쉽도록 +1 이렇게 작성해야한다.

print()

count2 = 10
while count2 > 5:
    #print(count2) 여기다가 작성하면 줄어들지 않은 상태로 출력부터 되기에
    # 10 9 8 7 6 이 출력된다.
    count2 = count2 -1 #count2 -= 1
    print(count2) # 여기다가 작성하면 -되고 출력되기에 98765이렇게 출력됨


#아이스크림 사먹기
'''
우리가 가진 돈 : 5000
아이스크림 : 1000
아이스크림을 2번 사먹어서
아이스크림을 사먹었다! 라는 텍스트가 2번 출력되게 작성해보기 
'''
money = 5000
ice_count = 1
while money > 3000:
    print(f"아이스크림을 {ice_count}번 사먹었다!")
    money -= 1000
    ice_count += 1
    print(f"남은 금액은{money}원 밖에 없어ㅜㅜ")
# 조건이 거짓이 되면 끝남

