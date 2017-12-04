# the part after `#` is “comment”.
# here we define a `say_hello` “function” which accepts an “argument” `name`.
def say_hello(name):
    # the indents distinguish the lines in or out of the function.
    # in this function, we call a bulit-in function `print` with an argument.

    # `'Hello, {}!'` is a string.
    # `.format` is its “method”, method is a function belonging an “object”.
    # we give `name` as an argument of the format.

    print('Hello, {}!'.format(name))


# `if` is used for conditional execution.
# `__name__` is a bulit-in “variable”, it will be the name of a “module”.
# if it is executed directly, it will be `'__main__'`.
if __name__ == '__main__':

    # call the function we just defined
    say_hello('Mosky')
