with open('file.txt', 'r') as file:
    lines = file.read().split("\n")
    lines.sort()
    count1 = len(lines)
    unique_lines = list(set(lines))
    count2 = len(unique_lines)


print("전체 정렬: ", lines)
print("전체 개수: ", count1)
print("중복을 제거하고 남은 개수: ", count2)

# f.read().split("\n")

# with open("file.txt", "r") as f:
#     color_list = []
#     for i in f.readlines():
#         color_list.append(i.replace("\n",""))

# color_list.sort()
# print("전체 정렬: ", color_list)
# print("전체 개수: ", len(color_list))
# print("중복을 제거하고 남은 개수: ", len(set(color_list)))
