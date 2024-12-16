set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# -연산자를 사용하여 차집합 구하기
diff_set = set_a - set_b
print(diff_set)  # 출력: {1, 2}

# difference() 메서드를 사용하여 차집합 구하기
diff_set = set_a.difference(set_b)
print(diff_set)  # 출력: {1, 2}

#음악과 역사반이 있는데 음악 공부하지만 역사는 공부하지 않는 학생을 찾아보자
music_students = {"알라딘", "오로라", "자스민"}
history_students = {"오로라", "자스민"}

# 음악만 공부하는 학생 ( - )
only_music = music_students - history_students
print("음악만 공부하는 학생:", only_music)  # 출력: {'알라딘'}

# 음악만 공부하는 학생 ( difference() )
only_music_method = music_students.difference(history_students)
print("음악만 공부하는 학생:", only_music)


