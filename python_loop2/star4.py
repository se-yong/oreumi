n = int(input())

for i in range(1, n+1):
    print(" " * (i-1) + "*" * (n + 1 - i))


# n = 5 일 경우
# " " --> i - 1 --> 0 ~ 4
# "*" --> n + 1 - i --> 6 - 1 줄어들면서 곱하기

# *****
#  ****
#   ***
#    **
#     *