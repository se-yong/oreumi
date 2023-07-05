# 2753

# 4의 배수이면서 100의 배수 , 400배수는 괜춘

year = int(input())

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('1')
else:
    print('0')