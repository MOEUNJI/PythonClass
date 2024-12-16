'''
num = 7 #우리가 일반적으로 사용하던 변수
nums = [0,1,2,3] #여러개의 데이터를 묶은 리스트
'''

numbers = [0,1,2,3] #숫자리스트
alphabets = ['a','b','c'] #문자리스트
bools_type = [True,True,True] #논리값 리스트
greetings = ["hello","오늘은 파이썬","9일째"] #문자열리스트


mixed_list = [1, "apple", 3.14, True] #숫자, 문자, 논리값 혼합리스트
print(mixed_list)
print(mixed_list[1])
'''
1 = 정수형(int)
2 = "apple": 문자열(str)
3 = 3.14: 실수형(float)
4 = True: 불리언(bool)
'''

print()

list_in_list = [1, [2, 3], "hello", [True, False]]
print(list_in_list)
print(list_in_list[1][1])

print()

names = ["kim","lee","park","choi","mo"]
print(names[-1])
print(names[-2])

text = "python"
print(text[-1])
print(text[-2])