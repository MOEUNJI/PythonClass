set_a = {1,2,3,4}
set_b = {3,4,5,6}
print(set_a) # {1, 2, 3, 4}
print(set_b) # {3, 4, 5, 6}

#intersection() 메서드를 사용하여 두 세트의 교집합을 찾기
insersection_AandB = set_a.intersection(set_b)
print(insersection_AandB) # {3, 4}

# &연산자를 사용하여 두 세트의 교집합 찾기
and_AandB = set_a & set_b
print(and_AandB) # {3, 4}

#문자열도 가능할까요?
'''
과일바구니에 딸기 오렌지 체리가 있어요!
그런데 내가 좋아하는 과일은 포도, 오렌지, 딸기 입니다.
공통되게 겹치는 과일을 두가지 방법으로 출력해보도록 할게요!
'''
set_fruits = {"strawberry","orange","cherry"}
set_favorites = {"grape","orange","strawberry"}

#& 연산자로 교집합 구하기
and_fruits = set_fruits & set_favorites #{'strawberry', 'orange'}
intersection_fruits = set_fruits.intersection(set_favorites) #{'strawberry', 'orange'}
print(and_fruits)
print(intersection_fruits)
