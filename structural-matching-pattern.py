# only available in Python 3.10+
# the match keyword works like a switch statement, except it can also match with patterns, not just values


def example(coords):
    # values in those positions in the input tuple will be assigned to variables 'x' and 'y'
    # hence pattern-matching, not just value-matching
    match coords:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Horizontal line at y = {y}")
        case (x, 0):
            print(f"Vertical line at x = {x}")
        case (x, y) if x == y:
            print(f"X = Y")
        case (x, y) if abs(x) == abs(y):
            print("|X| = |Y|")
        case (_, _):
            print("Valid coordinates")
        case _:
            print("Invalid coordinates.")


example((3, 7))


def example_two(some_list):
    # same as above
    match some_list:
        case [_]:
            print("One element")
        case [_, _]:
            print("Two elements")
        case [x, y, z]:
            print(f"Three elements: {x}, {y}, {z}")
        case [x, y, z, *a]:
            print(">=three elements")
        case _:
            print("None")


example_two([1, 2, 3, 4])
