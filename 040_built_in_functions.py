# https://docs.python.org/3/library/functions.html

# types

print('int()       ->', int()))  # -> 0
print('int(3)      ->', int(3)))
print('int(3.14)   ->', int(3.14)))  # truncates towards zero
print("int('3')    ->", int('3')))
print("int('3.14') -> ValueError")
print("int('x')    -> ValueError")
print('int(None)   -> TypeError')
print('int([3.14]) -> TypeError')
print()

print('float()       -> {!r}'.format(float()))  # -> 0.0
print('float(3)      -> {!r}'.format(float(3)))
print('float(3.14)   -> {!r}'.format(float(3.14)))
print("float('3')    -> {!r}".format(float('3')))
print("float('3.14') -> {!r}".format(float('3.14')))
print("float('x')    -> ValueError")
print('float(None)   -> TypeError')
print('float([3.14]) -> TypeError')
print()

print('str()       -> {!r}'.format(str()))  # -> ''
print('str(3)      -> {!r}'.format(str(3)))
print('str(3.14)   -> {!r}'.format(str(3.14)))
print("str('3')    -> {!r}".format(str('3')))
print("str('3.14') -> {!r}".format(str('3.14')))
print("str('x')    -> {!r}".format(str('x')))
print("str(None)   -> {!r}".format(str(None)))
print("str([3.14]) -> {!r}".format(str([3.14])))
print()

b = b'\xe6\x98\xaf\xe9\xa7\xad\xe5\xae\xa2\xef\xbc\x81'
print("str(b, 'utf-8') -> {!r}".format(str(b, 'utf-8')))
print()

print("list()  -> {!r}".format(list()))
print("tuple() -> {!r}".format(tuple()))
print("set()   -> {!r}".format(set()))
print()

print("list('apple')  -> {!r}".format(list('apple')))
print("tuple('apple') -> {!r}".format(tuple('apple')))
print("set('apple')   -> {!r}".format(set('apple')))
print()

print("{{'a': 1, 'b': 2}}         -> {!r}".format({'a': 1, 'b': 2}))
print("dict(a=1, b=2)             -> {!r}".format(dict(a=1, b=2)))
print("dict([('a', 1), ('b', 2)]) -> {!r}".format(dict([('a', 1), ('b', 2)])))
print()

print("iter('seq') -> {!r}".format(iter('seq')))
print("iter(iter('seq')) -> {!r}".format(iter(iter('seq'))))
print()

# math

print('abs(-3.14) -> {!r}'.format(abs(-3.14)))
print('round(3.14, 1) -> {!r}'.format(round(3.14, 1)))
print()

# https://docs.python.org/3/library/math.html
import math
print('math.floor(3.14) -> {!r}'.format(math.floor(3.14)))
print('math.ceil(3.14) -> {!r}'.format(math.ceil(3.14)))
print()

# .sort and sorted

chars = list('apple')
print('sorted(chars) -> {!r}'.format(sorted(chars)))
print('chars -> {!r}'.format(chars))
print()
chars.sort()
print('chars -> {!r}'.format(chars))
print()
