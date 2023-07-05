a = [1, 2, 3, 4, 5]

# b = a[::-1]
# print(b)

# a = [ i for i in range(1,6)]
# print(a[::-1])

left = 0
right = len(a) - 1

# while len(a) // 2 >= left:
while left < right:
    a[left], a[right] = a[right], a[left]
    left += 1
    right -= 1

print(a)

# a.reversed()
# print(a)

