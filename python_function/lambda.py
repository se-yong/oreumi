# def add(a, b):
#     return a + b

# add = lambda a, b: a+b
# result = add(2,3)
# print(result)

# 람다함수는 주로 다른 내장함수들과 함께 쓰인다.

# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x+1, numbers)) # map을 한후 map의 객체로 되어있기때문에 list로 형변환을 해주어야한다.
# print(squared)

students = [
    {"name": "이민영", "age": 23},
    {"name": "양승조", "age": 17},
    {"name": "문기원", "age": 25}
]
students.sort(key=lambda x:x["name"])
print(students)