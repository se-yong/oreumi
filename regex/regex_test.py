#  Regular Expression
import re

pattern = r'a[bdc]*d'
string = "ad, abcd, abbcd, acd"

result = re.findall(pattern, string)
print(result)