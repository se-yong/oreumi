# 10988

# word = list(str(input()))

# if list(reversed(word)) == word:
#     print(1)
# else:
#     print(0)
    

# word = input()

# 글자의 길이
# word_len = len(word)

# 양 끝 글자부터 하나씩 비교
# flag =0
# for i in range(word_len // 2):
#    if word[i] != word[word_len -i -1]:
#        flag = 1
#        print(0)
#        break

# if flag == 0:
#     print(1)

# 파이썬 슬라이싱
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = num_list[::-1]
print(a)