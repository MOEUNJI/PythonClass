'''
1. and : 연산자를 기준으로 왼쪽과 오른쪽 값이 모두 True일때만 True를 반환
        나머지는 모두 False 를 반환
        그리고~ 라고 생각하면 됨 모두 일치해야함
2. or : 연산자를 기준으로 왼쪽과 오른족 값중 하나라도 True이면 True를 반환
        둘다 False일때 False를 반환
        ~ 이거나 로 해석 둘 중 하나만 충족해도 됨
3. not : 뒤에 따라오는 논리값이 True이면 False를 반환(반대로)
        False라면 True를 반환
'''

num1 = 10
num2 = 20
num3 = 30
num_result = num1 < num2 and num2 < num3
print(num_result) #True
num_result = num1 > num2 & num2 < num3
print(num_result) # False
# 그리고 연산자는 결과를 모두 충족해야 True 나옴

num_result = num1 > num2 or num2 < num3
print(num_result) # True
# or 연산자는 둘중에 하나만 참이어도 True를 출력하니 True가 나옴

num_result = num1 > num2 or num2 > num3
print(num_result) # 둘 다 틀렸으니 False반환

false = False
print(false) #False를 넣었으니 False가 나옴
print(not false) #False를 넣고 not을 이용해 반대값을 출력 True 나옴
#주의할 점은 변수 자체의 값은 변하지 않는다는 것이다!!

print()

true = True
print(true) #true
print(not true) #False
print(true) #true 즉 not을 사용해도 변수 자체의 값은 변하지 않는다





