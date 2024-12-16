class NameError(Exception):
    def __init__(self):
        super().__init__("사람의 이름에는 숫자가 들어갈 수 없습니다.")

    #문자열 안에 숫자가 들어있는지 확인하기
    def is_there_digit(str):
        for temp in name:
            if temp.isdigit():
                return True
        return False

    try:
        name = input("이름을 입력하세요 : ")

        if is_there_digit(name):
            raise NameError

    except NameError as e:
        print(e)
    finally:
        print("프로그램을 종료합니다. ")
