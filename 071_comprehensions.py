from pprint import pprint

print('List Comprehensions:')
print([i for i in range(3)])
print([i for i in range(3) if i % 2 == 0])
pprint([
    (i, j)
    for i in range(3)
    for j in range(3)
])
print()

print('Set Comprehensions:')
print({i for i in range(3)})
print({i for i in range(3) if i % 2 == 0})
pprint({
    (i, j)
    for i in range(3)
    for j in range(3)
})
print()

print('Dict Comprehensions:')
print({i: chr(65+i) for i in range(3)})
print({i: chr(65+i) for i in range(3) if i % 2 == 0})
pprint({
    (i, j): (chr(65+i), chr(65+j))
    for i in range(3)
    for j in range(3)
})
print()
