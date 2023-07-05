# fruits = ["사과", "수박", "배"]
# for fruit in fruits:
#     print(fruit)

# fruits = ["사과", "수박", "배"]
# prices = [2500, 15000, 5000]
# for idx, x in enumerate(fruits):
#     print(idx+1, x)

# fruits = ["사과", "수박", "배"]
# prices = [2500, 15000, 5000]
# amounts = [5, 6, 3]
# for fruits, prices, amounts in zip(fruits, prices, amounts):
#     profit = prices * amounts
#     print(fruits, prices, amounts, profit)

# for i in reversed(range(0, 10)):
#     print(i)
    
# a = ["사과", "수박", "배"]    
# for i in reversed(a):
#     print(i)

# with open("test.txt", "r") as f:
#     for i in f.readlines():
#         print(i)

# with open("test.txt", "r", encoding='utf-8') as f:
#     text = f.read().split('\n')
#     for idx, line in enumerate(text):
#         name, score = line.split(" ")
#         print(f'{idx+1}번째 학생: {name}, 점수: {score}')

# for i in range(0, 10000):
#     if i == 6000:
#         print(i)
#     print(i)

# a = "Hello World!"
# cnt = 0
# for i in a:
#     cnt+=1
# print(cnt)

# a = ["1", "2", "3", "4", "5"]
# sum = 0
# for i in a:
#     sum += int(i)
# print(sum)4

# a = input("팩토리알 입력:")
# factorial = 1
# for i in range(1, int(a)+1):
#     factorial *= i
# print(factorial)


# n = int(input(""))

# for i in range(1, 10):
#     print(n, '*', i, '=', n*i)

# n = int(input(""))

# for i in range(1, 10):
#     result = n * i
#     print(f'{n} * {i} = {result}')

a = int(input(""))
for i in range(1, a+1):
    b, c = input("").split(" ")
    print(int(b) + int(c))