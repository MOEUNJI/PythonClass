#빈 딕셔너리 생성
friends = {}

#딕셔너리에 정보 추가하기
friends["도현"] = 19
friends["소민"] = 27
print(friends)
print(friends["소민"])

#소민이의 나이를 25살로 수정하기
friends["소민"] = 25
print(friends["소민"])

#딕셔너리에서 소민 삭제
del friends["소민"]
print(friends)

#딕셔너리 초기화
friends.clear()
print(friends)
