class Student:

    # 클래스 변수 선언 방법 : 클래스 변수명 = 값
    subject = "music"

    # subject 매개변수, 속성 삭제
    def __init__(self,name,ban):
        self.name = name
        self.ban = ban

    def introduce(self):
        print(f"안녕하세요 제 이름은 {self.name}입니다.")
        print(f"저는 {self.ban}반 입니다.")
        print(f"1교시 수업은 {self.subject}입니다.")
        print()

    def talk_subject(self):
        print(f"저는 {self.ban}반 {self.name}입니다.")
        if(self.subject == "music"):
            print(f"1교시 수업은 그대로 {self.subject} 입니다.")
        else:
            print(f"1교시 수업은 변경되어 {self.subject}입니다.")

#subject 매개변수 삭제
kelly = Student("kelly",1)
amily = Student("amily",1)
tom = Student("tom",1)

# 1반 학생 3명의 객체 생성
kelly.introduce()
amily.introduce()
tom.introduce()

#===============여기까지 기본구조 작성 완료==================
#===============클래스 변수 사용할 땐 주석처리 하기===========
#kelly와 amily의 과목 변경
# kelly.subject = "history"
# amily.subject = "history"

#세 학생의 과목 안내
# kelly.talk_subject()
# amily.talk_subject()
# tom.talk_subject()

#====================클래스 변수 사용=====================
Student.subject = "history"
kelly.talk_subject()
amily.talk_subject()
tom.talk_subject()

'''
같은 반에 속한 세명의 학생 객체를 생성한 후 모두 1교시를 music으로 설정했다가
켈리와 에밀리만 1교시를 변경했다.
그 결과 톰은 여전히 1교시가 음악시간인 줄 안다.
만약 수백명의 데이터를 바꿔야 한다면? 하나하나 바꿔줄 수 있을까?
시간낭비일 뿐만 아니라, 데이터 누락의 가능성도 생기겠죠?
이런 문제를 해결하기 위해 클래스 변수라는 개념을 사용하면 된다.
클래스 변수는 같은 클래스로 생성된 모든 객체가 공유하는 변수라고 설명했죠~?
즉 변수의 값을 변경하게 되면 해당 클래스에 속한 모든 객체는 자동으로
데이터가 변경될겁니다.
'''





