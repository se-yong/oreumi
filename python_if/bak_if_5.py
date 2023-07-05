# 2525

# A, B = map(int, input().split())
# C = int(input())

# A += C // 60
# B += C % 60

# if(B >= 60):
#     B -= 60
#     A += 1

# if(A >= 24):
#     A -= 24
    
# print(A, B)

H, M = map(int, input().split())
timer = int(input())

h = timer // 60
m = timer % 60

H += h
M += m

if M > 59:
    M -= 60
    H += 1

if H > 23:
    H -= 24
    
print(H, M)