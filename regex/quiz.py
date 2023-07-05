import re

# text = "안녕하세요. 저의 전화번호는 !-010-1234-5678-!입니다. 다른 전화번호는 !-02-987-6543-!입니다. 125!22%13. 지역번호가 155542-10-1"

# phone_numbers = re.findall(r"!\-(\d{2,3}\-\d{3,4}\-\d{4})\-!", text)
# print(phone_numbers)


# pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# string = "안녕하세요. 이메일 주소는 abc@example.com입니다. 다른 이메일은 def@hcu.co.kr이고, xyz@hotmail.net도 있습니다."

# result = re.findall(pattern, string)
# print(result)

# pattern = r"(?:https?://|www\.)\S+"
pattern = r"[\w//]+\.[\w/.]+\.[a-z/]+"
string = "문장 속에는 다양한 URL이 있습니다. https://www.example.com/, http://subdomain.example.co.kr/, www.google.com, ftp://fileserver.example.org, 이렇게 다양한 형식의 URL이 있습니다."

result = re.findall(pattern, string)
print(result)
