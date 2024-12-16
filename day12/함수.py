'''
def 함수이름():
    코드1
    코드2
    코드3
'''

def hello():
    print("안녕하세요")
    print("저는 안나입니다. ")
    print("엘사 동생이에요")
'''
우리 여태까지는 이렇게 작성하고 바로 쉬프트 + 10 으로 실행시키면 나타났는데 함수는 나타나지 않아요
우리는 함수를 호출해야합니다.

'''
hello()


colors = ["red", "orange", "yellow", "green", "skyblue"]
#색상리스트 생성
index = 0 # 초기 index변수 설정(처음에는 0이므로 처음 색상인 red를 뜻할것)

def change_color(): #배경색을 바꾸는 기능을 담은 함수를 생성
    global index
    # 함수 밖에 있는 index라는 변수를 가져다가 수정하고 싶으면 글로벌!
    if index >= len(colors):
        #index가 colors의 리스트의 길이보다 같거나 그다면
        index = 0 #인덱스를 0으로 변경해라.
        #만약 index가 5보다 크거나 같아지면, 리스트의 끝을 넘어가므로 다시 처음 색상(index = 0)으로 돌아갑니다.
    print(f"배경색을 {colors[index]}로 변경합니다.")
    # 현재 index에 해당하는 색상을 선택하여 출력합니다. index = 0일 때는 red가 출력됩니다.
    index += 1
    # 색상을 출력한 후에는 index를 1 증가시켜 다음 색상을 가리키도록 합니다.
    # 예를 들어, index = 0에서 1을 더하면 index = 1이 되고,
    # 다음번 호출에서 colors[1]인 "orange"가 선택됩니다.

change_color()
change_color()
change_color()
#호출할때마다 "red", "orange", "yellow", "green", "skyblue" 색이 바뀌고
#스카이 블루가 지나면 다시 red가 출력될 것
