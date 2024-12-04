# composition of functions
def g(b):
    def f(a):
        c = 3
        return a + b + c
    return f


print(g(10)(100))
print(g(20)(100))
