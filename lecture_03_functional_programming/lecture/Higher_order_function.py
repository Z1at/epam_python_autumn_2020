# Функция высшего порядка
def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def power(a, b):
    return a ** b


def highest_function(a, b, functions):
    results = [
        (f, f(a, b))
        for f in functions
    ]

    results = sorted(results, key=lambda c: c[1], reverse=True)
    return results


print(highest_function(2, 4, [add, mul, power]))
########################################################################################################################


b = 10


def f(a):
    c = 3
    return a + b + c


def g(a, b):
    return f(a)


print(g(100, 1))
