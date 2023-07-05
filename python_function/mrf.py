from functools import reduce

# map(함수, 리스트 or 튜플)


# numbers = [1, 2, 3, 4, 5]
# sum = reduce(lambda x, y: x+y, numbers) 
# print(sum)

# numbers = [1, 2, 3, 4, 5]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

numbers = ['lettet', 'bigger']
result = list(map(lambda x:x.upper(), numbers))
print(result)