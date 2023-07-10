# 그리디 알고리즘

N, K = map(int, input().split())

coin_lst = list()

for i in range(N):
    coin_lst.append(int(input()))
    
count = 0
for i in reversed(range(N)):
    count += K // coin_lst[i] # 동전을 사용했다.
    K = K % coin_lst[I] # 다음 동전 사이즈로 다시 계산하기위해 나머지를 남겨줌

print(count)