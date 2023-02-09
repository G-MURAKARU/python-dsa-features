def superDigit(n, k):
    # Write your code here
    if len(n) == 1:
        return int(n)

    new = sum(int(num) for num in n)

    new *= k

    return superDigit(n=str(new), k=1)
