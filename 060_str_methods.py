# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

sentence = 'Python is a cool programming language.'
words = sentence.split(' ')

print("sentence.split(' ') -> {!r}".format(sentence.split(' ')))
print("' '.join(words)     -> {!r}".format(' '.join(words)))
print()

print("'zh_TW'.partition('_') -> {!r}".format('zh_TW'.partition('_')))
print()

print("'Mosky.Liu@gmail.com'.lower() -> {!r}".format(
    'Mosky.Liu@gmail.com'.lower()
))
print("'report'.capitalize()         -> {!r}".format('report'.capitalize()))
print()

print("'Mosky Liu'.startswith('Mosky') -> {!r}".format(
    'Mosky Liu'.startswith('Mosky')
))
print("'output.txt'.endswith('.txt')   -> {!r}".format(
    'output.txt'.endswith('.txt')
))
print()
