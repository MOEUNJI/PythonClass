'''
def 함수이름(매개변수1,매개변수2...):
    코드1
    코드2
'''

#함수선언
def hello(name):
    print("안녕하세요 제 이름은" ,name, " 입니다.")

hello("제니") #안녕하세요 제 이름은 제니  입니다.
hello("지수") #안녕하세요 제 이름은 지수  입니다.

print()

#함수선언
def plus(a,b):
    print(a+b)

plus(10,20) #30
plus(5,20) #25
plus(3,50) #53

print()

def student(name, age):
    print(f"안녕하세요 저는 {name} 입니다.")
    print(f"나이는 {age} 실 입니다.")

student("모은지",20)
student("홍길동",19)
student("김도현",25)