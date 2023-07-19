from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = (len(queue1)) * 4
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    total = tot1 + tot2

    if total % 2 != 0:
        return -1

    while True:
        if tot1 > tot2:
            target = queue1.popleft()
            queue2.append(target)
            tot1 -= target
            tot2 += target
            answer += 1
        elif tot1 < tot2:
            target = queue2.popleft()
            queue1.append(target)
            tot1 += target
            tot2 -= target
            answer += 1
        else:
            break
        if answer == limit:
            answer = -1
            break
    return answer


# from collections import deque

# def solution(queue1, queue2):
#     queue1 = deque(queue1)
#     queue2 = deque(queue2)
#     sum_q1 = sum(queue1)
#     sum_q2 = sum(queue2)
#     length = len(queue1)
#     if (sum_q1 + sum_q2) % 2 != 0:
#         return -1
    
#     for count in range(length * 8):
#         if len(queue1) > 0 and len(queue2) > 0:
#             if sum_q1 > sum_q2:
#                 first = queue1.popleft()
#                 queue2.append(first)
#                 sum_q1, sum_q2 = sum_q1 - first, sum_q2 + first
#             elif sum_q2 > sum_q1:
#                 first = queue2.popleft()
#                 queue1.append(first)
#                 sum_q1, sum_q2 = sum_q1 + first, sum_q2 - first
#             else:
#                 return count

#     return -1