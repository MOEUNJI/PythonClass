sum = 1+2+3+4+5

sum = 0
sum += 1
sum += 2
sum += 3
sum += 4
sum += 5

nums = [1,2,3,4,5] #더할 리스트 생성
sum = 0 #초기값 설정
for nums_for in nums: #반복문 생성 nums_for는 nums의 개수만큼 접근할것
    sum += nums_for # 0인 sum에 반복되며 바뀌는 숫자들을 더해줌
print(sum) #위 코드로 인해 더해진 값을 출력함


'''
for 변수 in range(start,stop,step):
    실행할 코드
'''
for range_for in range(5):
    print(range_for)

print("=============================")

for range_for2 in range(2,6):
    print(range_for2)

print("=============================")

for range_for3 in range(1,10,2):
    print(range_for3)

print("=============================")

for range_for4 in range(10, 0, -2):
    print(range_for4)

print("=============================")

total = 0
for range_for5 in range(1, 6):  # 1부터 5까지
    total += range_for5 # 1부터 5까지 쌓으면서 값을 대입해줌
print("합계:", total)

print("=============================")

fruits = ["apple","banana","cherry"] #리스트 생성
for range_for6 in range(len(fruits)):
    # len(fruits) : len()함수는 리스트의 길이(요소개수)를 반환한다
    # 여기서 fruits 리스트는 3개의 요소가 있으니 len(fruits)은 3을 반환.
    # range() 함수는 숫자범위를 생성한다.
    # range(len(fruits)) : 숫자범위가 즉 과일의 개수가 되는것이다
    # range(3)이라고 작성하는것과 동일하다.
    print(f"인덱스 {range_for6}: {fruits[range_for6]}")

print("=============================")
#10까지 range() 함수로 출력하는데 짝수만 출력해주세요~
for i in range(2, 11, 2):  # 2부터 10까지 2씩 증가
    print(i)
