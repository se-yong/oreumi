# python에서는 오버로드가 없다.(다른 언어에서는 있음)

def add(a, b):
    return a+b

def add(a, b, c):
    return a+b+c

print(add(2, 3))

# 파이썬에서는 이름이 같을 때, 가장 최근에 정의된 함수에서만 불러온다.
# 동일한 이름으로 서로 다른 매개변수를 가진 함수를 여러개 사용하는 것