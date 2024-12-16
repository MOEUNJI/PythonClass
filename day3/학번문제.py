#학번 입력받기
student_id = input("5자리 학번을 입력하세요 : ")

#문자열 인덱싱과 슬라이싱으로 학년, 반, 번호 추출
grade = student_id[0] # 학번의 첫 번째 문자
class_num = student_id[1:3] #인덱스번호 1부터 3-1(2)까지 # 학번의 두 번째와 세 번째 문자
student_num = student_id[3:5] #인덱스번호 3부터 5-1(4)까지 # 학번의 네 번째와 다섯 번째 문자

#결과 출력
print(f"{grade}학년 {class_num}반 {student_num}번 ")