# 10811

# n,m = map(int, input().split())
# basket = [i for i in range(1,n+1)]
# temp = 0
# for x in range(m):
#     i,j = map(int, input().split())
#     temp = basket[i-1:j]
#     temp.reverse()
#     basket[i-1:j] = temp

# for x in range(n):
#     print(basket[x],end=" ")

n, m = map(int, input().split())

bucket_list = [i for i in range(1, n + 1)]
# bucket_list = [1, 2, 3, ....... , n]

for _ in range(m):
    i, j = map(int, input().split())
    bucket_list[i - 1 : j] = bucket_list[i - 1 : j][::-1]

print(*bucket_list)

# 인덱스 자체는 0번부터 시작하므로 i - 1부터 j까지 뒤집는다.
# 인덱스는 i - 1 번을 지정해줘야 한다.
# j번까지 뒤집기 위해서