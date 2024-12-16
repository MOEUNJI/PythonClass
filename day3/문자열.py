name1 = "mo" #큰따옴표 사용
name2 = 'eun ji' #작은따옴표 사용
name3 = '''mo eun ji''' #삼중따옴표 작은따옴표
name4 = """MO EUN JI""" #삼중따옴표 큰따옴표
num = "100" #숫자처럼 보이지만 문자열이다 따옴표로 묶었기 때문에!
null_string = "" #비어있다면 False로 간주한다.

#문자열 안에 작은따옴표 큰따옴표 주의!
str1 = "Park's Bakery" # 's 부분에 "를 쓰면 안 된다는 거!
str2 = 'eunji say "so funny"' # 큰따옴표를 사용하고 싶으면 겉을 작은걸로 감싸야함

#문자열 연산
first_name = "MO"
last_name = " EUN JI"
full_name = first_name + last_name # 더하기 연산자로 문자열을 합친다
print(full_name)

#문자열 반복(같은 문자열을 여러번 출력)
class_name = 'Python '
print(class_name*5)

#곱하기가 된다면 나눗셈도 될까? ( 5개로 늘어난 class_name을 가지고 실험하기!)
#print(class_name/5) #Python이 한 번 출력될 거 같지만 에러가 남
#즉 문자열 연산에서는 더하기와 곱하기만 가능하다는점!!!!!!


#문자열인덱스
a = "apple"
first_char = a[0] # a 출력
third_char = a[3] # l 출력
print(first_char)
print(third_char)

#마이너스 인덱스
# 마이너스 인덱스는 문자열의 뒤에서부터 번호를 부여하는 방식입니다!
# 뒤에서 첫번째 문자를 -1로 표현해요
last_char = a[-1] # e 출력
second_char = a[-4] # p 출력 (-5 넣으면 a나올것)
print(last_char)
print(second_char)

#문자열슬라이싱
#변수명[start:stop:step] : 문자열 슬라이스의 기본 구조!
'''
start(시작인덱스):슬라이싱을 시작할 위치를 정한다. 생략이 가능하며 생략하면 0
stop(종료인덱스):슬라이싱을 종료할 인덱스번호+1
   (생략 가능하며,생략하면 마지막 인덱스+1 / stop의 값을 7로 설정하면 6이 된다)
step(증감폭):인덱스의 증가 또는 감소값을 지정, 기본값은 1이며 생략하면 1씩증감
'''

text = "I Love Pasta"
slicing1 = text[2:6] #인덱스번호 2부터 6-1(5)까지 / step은 기본값1씩 증가
print(slicing1)

# 파스타만 출력해주세요(문제)!
slicing2 = text[7:12] #인덱스번호 7부터 12-1(11)까지 출력
print(slicing2)

steping = text[7:12:2]
#인덱스 7부터 12-1(11)까지 출력되는데 2step 단위로 출력해라
# 즉 7부터 2씩 증가하며 출력함 7,9,11 이 출력됨! (Pasta - Psa출력될것)
print(steping)

first_lost = text[:6]#시작 인덱스를 생략한 경우 (I Love)
print(first_lost)

last_lost = text[6:]# 작성숫자부터 해당되니까 띄어쓰기를 포함한다.( Pasta)
print(last_lost)


#문자열 길이
python_text = "Python"
python_length = len(python_text)
print(python_length) # len 함수는 문자열의 길이를 정수로 반환한다 (6이 나올것)


"""
length 외 유용한 함수
1. 문자열을 대문자로 변환하는 upper()
2. 문자열을 소문자로 변환하는 lower()
3. 양 끝 공백을 제거하는 strip() 
"""

pizza = "i love pizza"
upper_pizza = pizza.upper()
print(upper_pizza)

lower_pizza = upper_pizza.lower()
print(lower_pizza)

cola = "    This is cola"
strip_cola = cola.strip()
print(strip_cola) # 앞뒤 공백만 제거!!!!

coca = "---This is coca"
strip_cola2 = coca.strip("-") # 작성하지 않으면 ---This is coca 이렇게 출력ㄴ
print(strip_cola2)
