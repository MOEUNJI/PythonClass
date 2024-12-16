try:
    list = [1,2,3,4]
    print(list[5])
except IndexError:
    print("인덱스 범위를 벗어났습니다.")