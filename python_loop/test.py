# b = 1
# a = 2

# a, b = b, a

# print(a, b)

# 튜플안에 리스트형식으로 되어있는 값을 변경 가능
# a = (1, 2, [1, 2, 3])
# a[2][2] = 1
# print(a)

# total = int(input())
# type = int(input())

# sum = 0

# for i in range(type):
#     a, b = map(int, input().split())
#     sum += a*b

# if total == sum:
#     print("Yes")
# else:
#     print("No")

# for _ in range(int(input())//4):
#     print("long", end=" ")
# print("int")

# import sys  

# t = int(sys.stdin.readline())

# for _ in range(t):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)

# t = int(input())
# for _ in range (1, t+1):
#     a,b = map(int, input().split())
#     print(f'Case #{_}: {a} + {b} = {a+b}')

# x = int(input())

# for i in range(x):
#     a = str(input())
#     print(a[0]+a[-1])

# 백준 1357
# x, y = input().split()
# x = int(x[::-1])
# y = int(y[::-1])
# print(int(str(x+y)[::-1]))

# 백준 1152
# a, b = input().split()
# a = int(a[::-1])
# b = int(b[::-1])
# if a > b:
#     print(a)
# else:
#     print(b)

# 백준 5622
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# a = input()
# time = 0
# for i in range(len(a)):
#     for j in dial:
#         if a[i] in j:
#             time += dial.index(j)+3
# print(time)

# 일일복습퀴즈(평균구하기)
n = int(input())
sum = 0
for i in  range(n+1):
    sum += i

avg = sum / n
print(avg)