'''
class 클래스명:
    클래스
    생성자
    메서드

클래스 정의하기
    * 클래스 이름은 대문자로 시작한다.
    * 클래스 내부에 메서드(함수)나 속성을 추가하여 동작을 정의한다.

속성 정의하기(__init__ 메서드)
    *__init__ 메서드는 객체가 생성될 때 자동으로 호출되는 생성자이다.
    * 생성자에서 객체의 초기상태(속성)을 설정한다.
    * self는 현재 생성되는 객체 자신을 가리키는 변수로, 클래스 내부 메서드에서
      항상 첫 매개변수로 전달된다.

행동 정의하기(메서드 추가)
    * 메서
    드는 클래스가 제공하는 기증(행동)을 정의한다.
    * 메서드도 항상 self를 첫 매개변수로 사용한다.

클래스 용어 정리
    1. 클래스 : 제품의 설계도
    2. 객체 : 설계도(클래스)를 통해 만든 제품
    3. 속성 : 클래스 안에 변수
    4. 메서드 : 클래스 안에 함수
    5. 인스턴스 : 메모리에 살아있는 객체
'''

class Person: #클래스 정의하기
    def __init__(self,name,age,nationality): #생성자로 속성을 생성함
        self.name = name #이름속성
        self.age = age #나이속성
        self.nationality = nationality

    def introduce(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 국적 : {self.nationality}.")

# Person 클래스 객체 생성
person1 = Person("모은지", 25,"Korea")
person2 = Person("Kelly", 23,"USA")

# 속성과 메서드 사용
print(person1.name)  # 모은지
print(person1.age)   # 25
person1.introduce()  # 안녕하세요, 제 이름은 모은지이고, 25살입니다.
person2.introduce()

#붕어빵클래스 만들기===========================================================
print()

class Fish_bread: # TV 클래스 생성
    def __init__(self,taste,count):
        self.taste = taste # 무슨맛
        self.count = count # 개수

    def making(self):
        print(f"{self.taste}맛 붕어빵 {self.count}개 나왔습니다~")

fish_bread1 = Fish_bread("팥",3)
fish_bread2 = Fish_bread("슈크림",2)
fish_bread3 = Fish_bread("피자",1)


fish_bread1.making()
fish_bread2.making()
fish_bread3.making()

#소멸자=========================================================
print()

class Animal:
    def __init__(self,name):
        self.name = name
        print(f"{self.name} 객체가 생성되었습니다.")

    def __del__(self):
        print(f"{self.name} 객체가 삭제되었습니다.")
        #소멸자는 객체가 더 이상 사용되지 않고 메모리에서 제거되기 전에 마지막으로 사용되는 코드

animal1 = Animal("고양이")
del animal1

'''
동작원리
소멸자는 객체가 삭제되거나 프로그램이 종료될 때 호출됩니다.
모든 객체를 수동으로 del로 삭제하지 않아도,
Python의 가비지 컬렉터(Garbage Collector) 가 알아서 필요 없는 객체를 삭제해요.
객체가 삭제되면 __del__ 함수가 작동된다.
'''

#소멸자로 파일 정리하기
#이 클래스(설계도)는 파일을 열고 내용을 쓰고 닫는 방법이 적혀있다.
class FileHandler:
    def __init__(self,filename):
        # 클래스의 설계도를 사용할 때 자동으로 실행되는 부분이다.
        #filename : 어떤 파일을 오픈할지 알려주는 매개변수
        self.file = open(filename,'w')
        # 매개변수로 받은 파일을 열고 쓰기모드로 내용을 쓸 준비를 한다.
        print(f"{filename} 파일을 열었습니다.")
        #출력메시지 : 파일이 정상적으로 열렸음을 확인하기

    def write_data(self,data):
        # 매개변수 data에 파일에 쓸 내용을 전달받을것임
        self.file.write(data)
        # 전달받은 내용을 파일에 작성한다.
        #파일은 __init__() 함수로 가장 먼저 실행되어 열려있다.

    def __del__(self):
        self.file.close()
        print("파일을 닫았습니다.")

handler = FileHandler("test.txt")
handler.write_data("hellowwwwww python")
del handler




