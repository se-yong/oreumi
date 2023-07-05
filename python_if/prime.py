# 소수

n = int(input())

is_prime = True # 소수 판별 플래그값

for i in range(2, int(n**0.5 + 1)):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print("소수이다!")
else:
    print("소수가 아님!")
