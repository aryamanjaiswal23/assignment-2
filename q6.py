def calc(*args, **kwargs):
    tot = 0

    for arg in args:
        if isinstance(arg, (int, float)):
            tot += arg

    for value in kwargs.values():
        if isinstance(value, (int, float)):
            tot += value

    return tot


print(calc(1, 2, 3, 4))
print(calc(1, 2, 3, num1=4, num2=5))
print(calc(num1=1, num2=2, num3=3))
