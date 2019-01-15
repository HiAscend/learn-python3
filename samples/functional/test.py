import functools

max2 = functools.partial(max, 8)

print(max2(5, 7, 9))

print(int('16'))
print(int('16', base=10))
print(int('16', base=16))

