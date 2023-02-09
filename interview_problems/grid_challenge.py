def gridChallenge(grid):
    # Write your code here
    other = [sorted(line.split()) for line in grid]
    other_col = [[other[j][i] for j in range(len(other))] for i in range(len(other[0]))]

    return next(("NO" for line in other_col if line != sorted(line)), "YES")


print(gridChallenge(["uxf", "vof", "hmp"]))
