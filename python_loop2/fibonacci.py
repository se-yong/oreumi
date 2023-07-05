# n = int(input())

# fib_list = [0, 1]
# curr = 0
# next = 1
# for _ in range(2, n+1):
#     fib_num = curr + next
#     fib_list.append(fib_num)
#     curr, next = next, fib_num

# print(fib_list)
n = int(input())

curr, next = 0, 1

for i in  range(2, n+1):
    curr, next = next, curr + next

print(next)
