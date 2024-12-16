'''
if 조건식:
    조건식이 참일때
else:
    조건식이 거짓일 때
'''

# 바나나
fruit = "바나나" # 딸기로 바꿔서 바나나 그닥 나오는거 보여주기
if fruit == "바나나":
    print("저는 바나나를 좋아해요")
else:
    print("바나나 그닥")

# 양수 음수
num = -3
if num >= 0:
    print("양수입니다.")
else:
    print("음수입니다.")


#성인 여부(미니문제)
age = 20
if age >= 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")

#7의 배수인지
number = 49
if number % 7 == 0:
    print("number는 7의 배수입니다")
else:
    print("number는 7의 배수가 아닙니다.")

#짝수 홀수
odd_even = 19
if odd_even % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
