# ASSIGNMENT EXPRESSION OPERATOR


def func(x):
    # do some long computation
    return x + 1


# DEFAULT CODE
if func(4) >= 5:
    print(func(4))

# MORE SENSIBLE WAY
y = func(4)
if y >= 5:
    print(y)

# CLEANER, PYTHONIC WAY (using walrus)
if (z := func(4)) >= 5:
    print(z)
