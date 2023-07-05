# def greet(name):
#     print("반갑습니다! {} 여러분".format(name))

# greet("oreumi")

def add(a, b):
    return a + b

def subtract(a, b):
    return a- b

def multiply(a, b = 2):
    return a * b

def sum(*args): # 가변 인자
    total = 0
    for i in args:
        total += i
    return total

def character_info(name, age):
    print("이름:", name)
    print("나이:", age)
    
def database_login(address, ip, database):
    pass



character_info(name="박세용", age=29)

