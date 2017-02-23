from pprint import pprint

print('Generator Comprehensions:')
print((i for i in range(10)))
print((i for i in range(10) if i % 2 == 0))
pprint((
    (i, j)
    for i in range(3)
    for j in range(3)
))
