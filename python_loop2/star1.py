# n = int(input())

# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ") # end=" " 은 줄바꿈을 막기위해서 사용
#     print()

lines = int(input())

for line in range(1, lines+1):
    for j in range(line):
        print("*", end="")
    print("")
    
# for line in  range(1, lines+1):
#     print("*" * line)
