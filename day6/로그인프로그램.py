id = input("아이디를 입력해주세요 : ")
password = int(input("비밀번호를 입력해주세요(숫자4) :"))

if id == "moeunji" and password == 1234:
    print("로그인 되었습니다")
elif id != "moeunji" and password == 1234:
    print("아이디 불일치")
elif id == "moeunji" and password != 1234:
    print("비밀번호 불일치")
else:
    print("아이디, 비밀번호 불일치 회원가입하러가기")
