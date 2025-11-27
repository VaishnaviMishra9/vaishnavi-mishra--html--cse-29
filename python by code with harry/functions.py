def greet(name):
    gr =" Hello" + name
    return gr
a = greet("tusha")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)