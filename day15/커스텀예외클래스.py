class NameError(Exception):  # 사용자 정의 예외 클래스
    def __init__(self):
        super().__init__("사람의 이름에는 숫자가 들어갈 수 없습니다.")

    # 문자열 안에 숫자가 들어있는지 확인하기 (staticmethod로 선언)
    def is_there_digit(name):
        for temp in name:
            if temp.isdigit():  # 숫자가 포함되어 있으면 True 반환
                return True
        return False

try:
    name = input("이름을 입력하세요: ")

    # 이름에 숫자가 포함되어 있는지 검사
    if NameError.is_there_digit(name):  # 클래스 메서드를 호출
        raise NameError

except NameError as e:
    print(e)
finally:
    print("프로그램을 종료합니다.")
