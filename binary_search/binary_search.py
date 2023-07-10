# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1

# # 예시 리스트
# numbers = [1, 4, 9, 16, 25, 31]

# # 타겟 값인 1을 찾는 이분 탐색 실행
# index = binary_search(numbers, 1)

# if index != -1:
#     print("찾는 값의 인덱스:", index)
# else:
#     print("찾는 값이 리스트에 없습니다.")

def binary_search(start, end, target, array):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

array = [1, 2, 3, 4, 5]
target = 0

result = binary_search(0, len(array) - 1, target, array)
print(result)