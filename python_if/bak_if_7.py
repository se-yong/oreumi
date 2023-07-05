# 10818

# a = int(input())
# b = list(map(int, input().split()))

# max_value = b[0]
# min_value = b[0]

# for num in b[1:]:
#     if num > max_value:
#         max_value = num
#     elif num < min_value:
#         min_value = num

# print(min_value, max_value)

a = int(input())

num_list = input().split(" ")
for idx, i in enumerate(num_list):
    num_list[idx] = int(i)
    
max = num_list[0]
min = num_list[0]

for i in num_list:
    if max < i:
        max = i
    if min > i:
        min = i
        
print(min, max)
