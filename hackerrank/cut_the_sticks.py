def cutTheSticks(arr):
    # Write your code here
    no_of_sticks = []
    while arr:
        no_of_sticks.append(len(arr))
        shortest_stick = min(arr)
        i = 0
        while i < len(arr):
            arr[i] -= shortest_stick
            if arr[i] == 0:
                arr.pop(i)
            else:
                i += 1

    return no_of_sticks
