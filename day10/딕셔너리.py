'''
{
    key1 : value1,
    key2 : value2 #이 쌍을 페어 또는 쌍이라고 부름
}
'''
from itertools import product

me = {
    "name" : "MoEunJi", # key : value
    "age" : 20,
    "phone" : "010-1234-5678",
    "class" : ["c언어", "python","java"]
}

my_phone = {
    "name" : "아이폰16",
    "price" : "1,400,000",
    "color" : "white",
    "storage" : "256GB"
}

print(me)
print(my_phone["color"]) #white
print(me["class"]) #['c언어', 'python', 'java']