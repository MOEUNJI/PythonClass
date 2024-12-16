# try:
#     list = [1,2,3,4]
#     print(list[5]) # 예외가 발생함
#     print("try구문 안에 예외 발생 후 코드")
# except IndexError as a:
#         print(a)
# print("try-except 구문 밖 코드")

'''
try:
    예외가 발생할 수 있는 코드
except:
    예외가 발생했을 때 수행되는 코드
finally: 
    예외 발생과 상관없이 항상 실행되는 코드
'''

try:
    f = open("test.txt","w") #파일 열기
    f.write("finally 실습중입니다.") # 파일에 데이터 작성
except EOFError as e:
    print(e)
    #EOFError : 파일에서 더 이상 읽을 데이터가 없음
finally:
    f.close() #파일 닫기

print(f.closed) #파일의 close상태 확인