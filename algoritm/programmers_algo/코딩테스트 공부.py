def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    time = 0
    for a,b,c,d,e in problems:
        max_alp = max(max_alp,a)
        max_cop = max(max_cop,b)
        time += e
    # 목표 알고력
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    INF = float('inf')
    dp = [[INF]*(max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j    ] = min (dp[i + 1][j    ],dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i    ][j + 1] = min (dp[i    ][j + 1],dp[i][j] + 1)

            for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp,next_cop = min(max_alp,i + alp_rwd), min(max_cop,j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop],dp[i][j] + cost)
    return dp[-1][-1] 

# 다른 답안 

# import sys
# def solution(alp, cop, problems):

#     alp_max = max(problems, key=lambda x:x[0])[0]
#     cop_max = max(problems, key=lambda x:x[1])[1]

#     dp = [[sys.maxsize] * (cop_max + 1) for _ in range(alp_max + 1)]
#     alp = min(alp, alp_max)
#     cop = min(cop, cop_max)

#     for i in range(alp, alp_max + 1):
#         for j in range(cop, cop_max + 1):
#             if i + 1 <= alp_max:
#                 dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
#             if j + 1 <= cop_max:
#                 dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

#             for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
#                 if i >= alp_req and j >= cop_req:
#                     next_alp, next_cop = min(alp_max, i + alp_rwd), min(cop_max, j + cop_rwd)
#                     dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)

#     return answer