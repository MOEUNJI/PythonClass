
class Parent:
    def cook(self):
        print("부모님이 요리를 완성했어요!")

class Child(Parent):
    def serve(self):#서빙 기능 생성!
        super().cook() # 부모님이 요리한것을 가져옴
        print("자식이 음료를 추가로 제공합니다.")

child = Child()
child.serve()

'''
super()를 간단히 정리
"부모님이 가진 기능을 쓰고 싶다"
→ super()를 써서 부모님(부모 클래스)의 기능을 호출합니다.

"부모님 기능에 내 일을 추가하고 싶다"
→ super()로 부모님의 일을 가져오고, 내 일을 추가로 작성합니다.
'''

#=====================인사하기==========================
print()

#슈퍼(부모)클래스
class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"안녕하세요, 제 이름은 {self.name}입니다.")

#서브(자식)클래스
class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)  # 부모님의 기능 가져오기(이름설정)
        self.classroom = classroom
        '''
        자식 클래스가 부모 클래스에서 상속받은 기능을 그대로 사용할 경우,
        부모 클래스의 __init__ 메서드가 자동으로 호출됩니다.
        자식 클래스에서 classroom 같은 추가 속성을 정의하지 않는다면,
        __init__ 메서드를 생략해도 부모 클래스의 생성자가 정상적으로 실행됩니다.
        '''

    def greet(self):
        super().greet() #부모클래스의 인사 기능 사용
        print(f"저는 {self.classroom}반 학생입니다.")
        #자식클래스에 self.name을 사용했지만 name이라는 생성자(속성)이
        # 없는 이유는 부모요소로 받아오고 있기 때문이다.


student = Student("철수",3)
student.greet()


