import time
#파이썬의 내장 모듈인 time을 가져오는 코드


def timer(pause_second,callback): #타이머 역할
    #pause_second: 몇 초 동안 기다릴지를 지정하는 숫자.
    #callback: 기다린 후에 실행할 함수.
    print("타이머 시작")
    print(f"{pause_second}초 뒤 요청하신 함수가 호출됩니다.")

    time.sleep(pause_second)#매개변수값
    #time.sleep(pause_second) : 프로그램을 pause_second만큼 멈춰서 기다리게 함
    #time.sleep(5) → 5초 동안 아무 작업도 하지 않고 기다림.
    callback()
    #pause_second에 입력한 초를 기다린 후 전달받은 함수를 실행해요.
    print("타이머 종료")

def callback():
    #타이머가 끝난 후 실행할 작업이에요.
    #여기서는 "요청한 함수 호출 완료"라는 문장을 출력하는 단순한 함수예요.
    print("요청한 함수 호출 완료")

timer(5,callback)
#pause_second = 5 → 5초 동안 기다림.
#callback = callback() → 기다린 후에 callback() 함수를 실행.