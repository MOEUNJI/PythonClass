'''
class 슈퍼클래스명:

class 서브클래스명(슈퍼클래스명):
'''

class Parent:
    def __init__(self,name):
        self.name = name

    def hello(self):
        print(f"안녕하세요 저는 {self.name}입니다.~")

class Child(Parent):
    def bye(self):
        print("안녕히 계세요~")

#부모요소 출력
parent = Parent("모은지")
parent.hello()

print()

#자식요소 출력
child = Child("김바보")
child.hello()
child.bye()


