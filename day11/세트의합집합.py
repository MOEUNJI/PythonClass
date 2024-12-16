set_a = {1, 2, 3}
set_b = {3, 4, 5}

# |연산자를 사용하여 합집합 구하기
union_set = set_a | set_b
print(union_set)  # 출력: {1, 2, 3, 4, 5}

# union() 메서드를 사용하여 합집합 구하기
union_set = set_a.union(set_b)
print(union_set)  # 출력: {1, 2, 3, 4, 5}


# 학원생 전원의 명단을 뽑아보자
students_math = {"엘사", "모아나", "라푼젤"}
students_science = {"엘사", "안나", "모아나"}

# |연산자를 사용하여 합집합 구하기
all_students = students_math | students_science  # 방법 1: | 연산자
print("모든 학생:", all_students)  # 출력: {'엘사', '라푼젤', '모아나', '안나'}

# union() 메서드를 사용하여 합집합 구하기
all_students_method = students_math.union(students_science)  # 방법 2: union 메서드
print("모든 학생:", all_students_method)  # 출력: {'엘사', '라푼젤', '모아나', '안나'}


