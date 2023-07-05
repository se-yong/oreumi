# 재귀함수

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

def outer_function():
    x = 10 # 2
    
    def inner_function():
        print(x) # 4

    inner_function() # 3

outer_function() # 1