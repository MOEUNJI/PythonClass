'''
비교연산자
1. > 왼쪽 값이 오른쪽 값보다 크다
2. < 왼쪽 값이 오른쪽 값보다 작다
3. >= 왼쪽 값이 오른쪽 값보다 크거나 같다
4. <= 왼쪽 값이 오른쪽 값보다 작거나 같다
5. == 왼쪽과 오른쪽의 데이터가 같다 ( = 하나는 대입 연산자이기 때문에 )
6. != 왼쪽 값과 오른쪽 값이 다르다

모든 조건은 맞으면 true, 틀리면 false를 반환한다.
'''

a = 10
b = 7

ab_result = a > b
print(ab_result) # True

ab_result2 = a < b
print(ab_result2) # False

ab_result3 = a >= b
print(ab_result3) # True

ab_result4 = a <= b
print(ab_result4) # False

ab_result5 = a == b
print(ab_result5) # False

ab_result5 = a != b
print(ab_result5) # True


print()

#문자열 비교
string1 = "Python"
string2 = "P" + "y" + "t" + "h" + "o" + "n"

string_result = string1 == string2
print(string_result) # True 출력

#문자열, 숫자형 비교

one = 1
first = "1"

type_result = one == first
print(type_result) #False

#다중연산자

z = 1
y = 2
x = 3
xyz_result = z < y < x
# 다른 언어에서는 <X 부분은 무시하는데 파이썬에서는 연산이 가능하다.
print(xyz_result) #True