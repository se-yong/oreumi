# max() 함수 이용하지 않고 반복문과 조건


a = [1, 2, 3, 4, 5]
max_value = a[0]  # 리스트의 첫 번째 값을 최대값으로 초기화 --> 리스트안의 값들이 만약 전부 음수일경우 최대값이 항상0으로 초기화 때문에 인덱싱 사용

for num in a:
    if num > max_value:
        max_value = num

print(max_value)