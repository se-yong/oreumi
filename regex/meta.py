import re

# pattern = r"b.t" # . => b 와 t 사이에 아무글자나 매칭시켜주는것(한 글자)
# string = "bat, bet, bit, but, baat, beet"

# pattern = r"ab+c" # a c 사이에 적어도 b가 한개이상있어야하며, b만 있어야한다.
# string = "ac, abc, abbc, abbbc, abdc"

# pattern = r"ab*c" # 0개 이상
# string = "ac, abc, abbc, abbbc, abdc"

# pattern = r"(ab)+"
# string = "abc, ababc, abababc, ab, aabbc"

# pattern = r"[aeiou]" # 대괄호 안에있는 어떠한 문자라도 매칭
# string = "apple, orange, banana"

# pattern = r"[0-9]"
# string = "1234567890"

# pattern = r"\d+" # + => 같은유형의 문자가 한개이상 반복되는 것을 찾아줌 
# string = "I have 10 apples and 5 bananas"

# pattern = r"\w+" # 특수문자를 제외한, 문자나 숫자를 전부 다 찾는것
# string = "Hello, World! 123"

# pattern = r"^Hello" # 캐럿, 해당문자가 시작되는 부분부터 매칭 확인
# pattern = r"hon!$" # 끝 부분 매칭 확인
# string = "Hello, World! Hello, Python!"

# pattern = r"a{1,}"
# string = "ab, abc, aabc, aaabc"

# pattern = r"a|b" # a 또는 b
# string = "ab, abc, aabc, aaabc"

pattern = r"(ab)+"
string = "ababc"

result = re.findall(pattern, string)
# result = re.match(pattern, string)
print(result)