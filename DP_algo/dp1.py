# 백준 24416

def fibonacci(n):
    dp=[0]*(n+1) # <--- 초기화 [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    dp[1],dp[2]=1,1 # [0 1 1 0 0 0 0 0 0 0 0 0 0 0]
    cnt=0
    for i in range(3,n+1):
        cnt+=1
        dp[i]=dp[i-1]+dp[i-2] # [0 1 1 2 3 5 ...]
    return dp[n], cnt

n = int(input())
count, count2 = fibonacci(n)
print(count, count2)