def minimum_grading_time(N, Times):
    Times.sort()  # 채점 시간 오름차순으로 정렬
    left, right = 1, N * Times[-1]  # 이진 탐색 범위 설정
    
    while left <= right:
        mid = (left + right) // 2
        total = 0
        
        # 각 멘토들이 mid 분 동안 채점할 수 있는 시험지의 개수를 계산
        for time in Times:
            total += mid // time
        
        # 채점할 수 있는 시험지의 개수가 N보다 크면 시간을 줄여야 함
        if total >= N:
            right = mid - 1
        else:
            left = mid + 1
    
    return left

# 입력 예시 처리
N = int(input())
Times = list(map(int, input().split()))

# 결과 출력
result = minimum_grading_time(N, Times)
print(result)