x = 10
print(x)

x = -x # 양수였던 10앞에 -를 붙여서 음수로 변경
print(x) # -10

x = -x # -10 에다가 -를 붙여서 --10이 된거임 -(-10) 하면 +로 바뀜
print(x) #10 출력

#그럼 이렇게 작성하면 어떻게 될까?
true = True #True라는 값은 숫자 1로 취급됨 ( 질문하기 True가 뭐냐고)
print(true)
print(-true)
print(true) # 값이 변한 건 아니다! 위에 코드는 일시적으로 저렇게 출력하는거임

