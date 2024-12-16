"""
조건연산자를 사용해서 국어, 영어, 수학 점수를 각각 입력받아
평균을 구하고 평균이 80점 이상이면 합격, 아니면 불합격을 출력
"""

#점수 입력받기
korean = int(input("국어점수를 입력해주세요 : "))
english = int(input("영어점수를 입력해주세요 : "))
math = int(input("수학점수를 입력해주세요 : "))

#평균점수 계산
average = (korean + english + math) / 3

result = "합격입니다" if average >= 80 else "불합격입니다."
print(f"평균 : {average:.2f}, 결과 : {result}")
#formatted string"**의 약자로, Python 3.6부터 지원됩니다.
#문자열 앞에 f를 붙이면, 문자열 안에서 중괄호 {}를 사용해 변수를 직접 삽입할 수 있습니다.
#.2f: 숫자를 소수점 두 자리로 포맷.

