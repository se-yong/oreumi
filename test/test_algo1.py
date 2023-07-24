def palindrome_check(text: str) -> bool:
    if text[::1] == text[::-1]:
        return True
    else:
        return False

def palindrome_check2(text: str) -> bool:
    for i in range(len(text) // 2):
        if text[i] != text[-i]:
            return False
    return True

def palindrome_check3(text: str) -> bool:
    if len(text) <= 2:
        return True
    
    if text[0] == text[-1]:
        return palindrome_check3(text[1:-1])
    else:
        return False

text = input()
functions = [palindrome_check, palindrome_check2, palindrome_check3]
for func in functions:
    print(func(text))