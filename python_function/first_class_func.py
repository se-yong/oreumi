# 일급함수

# def cat():
#     return "Meow"

# dog = cat
# print(type(dog))
# print(dog())

# 고차 함수

def apply_operation(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

result = apply_operation(multiply, 2, 3)
print(result)