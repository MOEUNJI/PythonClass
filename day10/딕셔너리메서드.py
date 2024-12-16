'''
1. keys() : 딕셔너리의 모든 key값들을 모아 리스트와 유사한 형태로 반환
2. values() : 딕셔너리의 모든 값을 반환
3. items() : 딕셔너리의 모든 키(key)와 값(value) 쌍을 반환합니다.
4. update(other_dict) : 딕셔너리에 다른 딕셔너리의 키-값 쌍을 추가하거나 덮어씁니다.

'''


print("keys()")
my_dict = {
    "name" : "kelly",
    "age" : 25,
    "city" : "New York"
}
keys = my_dict.keys() #my_dict의 모든 키들을 뽑아서 리스트처럼 보이게 만들어줌
print(keys)  # 결과: dict_keys(['name', 'age', 'city'])
print()


list = list(my_dict.keys()) #my_dict의 모든 키들을 리스트화
print(list)  # 결과: dict_keys(['name', 'age', 'city'])
print()

print("values()")
values = my_dict.values()
print(values)  # 결과: dict_values(['kelly', 25, 'New York'])
print()

print("items()")
items = my_dict.items()
print(items)
# 결과: dict_items([('name', 'Alice'), ('age''New York')])
print()

print("update()")
my_dict.update({"age":26,"hobby":"freediving"})
print(my_dict)
# 결과: {'name': 'kelly', 'age': 26, 'city': 'New York', 'hobby': 'freediving'}
# 키가 있다면 값을 변경하고, 키가 없다면 추가함
print()

#오름차순
print(sorted(my_dict)) #키만출력됨 ['age', 'city', 'hobby', 'name']
print(sorted(my_dict.items())) #[('age', 26), ('city', 'New York'), ('hobby', 'freediving'), ('name', 'kelly')]

#내림차순
print(sorted(my_dict,reverse=True)) #['name', 'hobby', 'city', 'age']
