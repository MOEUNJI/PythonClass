class Zoo:
    meat_lunch_time = 12
    vegetable_lunch_time = 13

    def __init__(self,name,type):
        self.name = name
        self.type = type

    def lunch_time(self):
        #점심시간을 클래스 변수에서 가져옴
        if(self.type == "초식동물"):
            return Zoo.vegetable_lunch_time
        else:
            return Zoo.meat_lunch_time

    def introduction(self):
        print(f"안녕하세요 저는 {self.name}이고,{self.type}입니다.")
        print(f"저는 {self.type}이라서 점심시간이 {self.lunch_time()}시 입니다.")
        print()

lion = Zoo("사자", "육식동물")
tiger = Zoo("호랑이", "육식동물")
elephant = Zoo("코끼리", "초식동물")
giraffe = Zoo("기린", "초식동물")

lion.introduction()
tiger.introduction()
elephant.introduction()
giraffe.introduction()

Zoo.meat_lunch_time += 1
Zoo.vegetable_lunch_time += 1

lion.introduction()
tiger.introduction()
elephant.introduction()
giraffe.introduction()



