import math


def encryption(s):
    # Write your code here
    s_list = list(s)
    while " " in s_list:
        s_list.remove(" ")

    length = len(s_list)

    sqroot = math.sqrt(length)
    rows = math.floor(sqroot)
    cols = math.ceil(sqroot)
    if (rows * cols) < length:
        rows += 1

    grid = [[] for _ in range(rows)]

    i = 0
    while i < rows:
        j = 0
        while j < cols:
            try:
                grid[i].append(s_list[(i * cols) + j])
            except IndexError:
                grid[i].append("")
            finally:
                j += 1
        i += 1

    encrypted = ""

    j = 0
    while j < cols:
        i = 0
        while i < rows:
            encrypted += grid[i][j]
            i += 1
        encrypted += " "
        j += 1

    return encrypted.rstrip()


print(encryption("chill out"))
