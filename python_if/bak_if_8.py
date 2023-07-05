# 2869

a, b, v = map(int, input().split())

# x = (v-b)/(a-b)
# if x == int(x):
#     print(int(x))
# else:
#     print(int(x) + 1)

day = (v-b)/(a-b)
print(int(day) if day == int(day) else int(day)+1)