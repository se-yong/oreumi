# a = int(input("숫자를 입력해주세요: "))

# for i in range(1, 101):
#     print(i)
#     if i == a:
#         print("종료!")
#         break # <---- for문 종료
# # ------ break 하면 뒤에는 실행 X

answer = 50

while True:
    guess = int(input("숫자를 맞춰보세요: "))
    
    if guess < answer:
        print("그것보다 큽니다!")
    elif guess > answer:
        print("그것보다 작습니다!")
    else:
        print("맞았습니다!")
        break