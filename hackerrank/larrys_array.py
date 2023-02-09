def larrysArray(A):
    # Write your code here
    length = len(A)
    index_count = 0

    while index_count <= length - 3:
        if A[index_count] != index_count + 1:
            old_index = A.index(index_count + 1)
            if old_index == length - 1:
                A[old_index - 2], A[old_index - 1], A[old_index] = (
                    A[old_index - 1],
                    A[old_index],
                    A[old_index - 2],
                )
            else:
                A[old_index - 1], A[old_index], A[old_index + 1] = (
                    A[old_index],
                    A[old_index + 1],
                    A[old_index - 1],
                )
        else:
            index_count += 1

    return "YES" if A == sorted(A) else "NO"
