str1 = "hello"
str2 = "world!"

print(str1 +" "+ str2)

str1 = "오르미 강의 너무 재밌다!" * 10
print(str1)

# 문자열 인덱싱
str1 = "여기서 a는 몇번째 일까요?"
print(str1[4])

str1 = "여기서 apple은 어디서부터 어딜까지일까요?"
print(str1[4:9]) # 4부터 9전까지
print(str1[9:]) # 9 다음부터
print(str1[:4]) # 4 전까지

str1 = "세고싶은 글자를 입력하세요."
print(len(str1))