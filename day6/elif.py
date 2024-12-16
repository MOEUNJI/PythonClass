'''
if 조건식1:
    조건식1이 참일때 실행할 코드
elif: 조건식2:
    조건식 1은 맞지 않고, 조건식2가 참일때 실행
elif: 조건식3
    조건식2는 맞지 않고 조건식3이 맞을 때 실행
else:
    모든 조건식1,2,3이 일치하지 않을 때 실행
'''

num = 0
if num > 0:
    print("양수입니다.")
elif num == 0:
    print("0입니다.")
else:
    print("음수입니다.")

# 점수 입력받기
score = int(input("점수를 입력해주세요: "))
# 입력받은 값은 문자열이므로 int()로 변환

# 조건문으로 학점 출력
if score >= 90:
    print("A학점 참 잘했어요!")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
else:
    print("F학점으로 재시험 당첨~")

