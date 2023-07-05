# 최대공약수
# a, b = input("").split(" ")
# a = int(a)
# b = int(b)
# while b != 0:
#     a, b = b, a % b

# print(a)

# 최소공배수
# 두 수를 곱하고 최대공약수로 나눈다.
# a, b = input("").split(" ")
# a = int(a)
# first_a = a
# b = int(b)
# first_b = b
# while b != 0:
#     a, b = b, a % b

# print(f'최대공약수: {a}')
# print(f'최소공배수: {first_a * first_b / a}')

# 소인수분해
# 소수 = 1 과 약수가 자기자신밖에없는 수 ex) 2, 3, 5 ,7 ,11, 13...
# 30 = 2 * 15
# 30 = 2 * 3 * 5

n = int(input("소인수 분해할 숫자를 입력해주세요:"))
factors = []
# n = 36
while n % 2 == 0:
    factors.append(2)
    n //= 2 # 몫 (정수형)
    # n /= 2 --> float(실수형)
# n = 9

i = 3
while i * i <= n:
    while n % i == 0:
        factors.append(i)
        n //= i
    i += 2
if n > 1:
    factors.append(n)

print(factors)