"""
    this is the "x" module
    the x module supplies one function, add_integer(). For example,

    >>> add_integer(2, 9)
    11
"""


def add_integer(a: int, b: int = 98) -> int:
    """
    add_integer computes arithmetic addition between two integers

    Args:
        a (int): first integer to add
        b (int, optional): second integer to add. Defaults to 98.

    Returns:
        int: sum of integers a and b

    >>> add_integer(2)
    100

    >>> add_integer(2, 10)
    12

    >>> add_integer(10.3)
    108

    >>> add_integer(100.9, -90.4)
    10

    >>> add_integer("tree")
    Traceback (most recent call last):
    TypeError: a must be an integer

    >>> add_integer(2, "tree")
    Traceback (most recent call last):
    TypeError: b must be an integer
    """

    def validate(num: tuple) -> int:
        var, val = num
        if not isinstance(val, (int, float)):
            raise TypeError(f"{var} must be an integer")
        else:
            return int(val)

    a = validate(("a", a))
    b = validate(("b", b))
    return a + b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
