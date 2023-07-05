# 9498

# n =int(input())

# A 90 ~ 100
# B 80 ~ 89
# C 70 ~ 79
# D 60~ 69
# 나머지 F

# if 90 <= n <= 100:
#     print("A")
# elif 80 <= n < 90:
#     print("B")
# elif 70 <= n < 80:
#     print("C")
# elif 60 <= n < 70:
#     print("D")
# else:
#     print("F")
score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")