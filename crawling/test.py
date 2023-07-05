# 10815

# 이진탐색 방법
n = int(input())
a = list(map(int, input().split()))
a.sort()

def binary_search(num):
    l = 0
    r = n-1
    while l <= r :
        mid = (l+r)//2
        if a[mid] == num :
            return 1
        elif a[mid] > num :
            r = mid - 1
            # 반 줄여주기 1
        else:
            l = mid + 1
            # 반 줄여주기 2
    return 0

input()
for num in list(map(int, input().split())):
    print(binary_search(num), end = ' ')

# 정규표현식 문제
# 1. 8글자 이상
# 2. 영어 대소문자, 숫자, 특수문자를 모두 포함
# 3. 공백은 포함되면 안됨

# import re

# text = "ABCdef123!@#"
# pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$"
# result = re.findall(pattern, text)
# print(result)