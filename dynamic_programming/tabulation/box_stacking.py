def find_max_height_stacked_boxes(boxes: list[tuple[int]]):
    """
    stack_boxes finds the maximum height of stacked boxes provided they are stacked
    in decreasing length and decreasing width

    Args:
        boxes (list[tuple[int]]): a list of all the boxes' dimensions

    Returns:
        int: the highest possible height
    """

    # sorting the boxes in decreasing length already fulfills one constraint - the length constraint
    # therefore we find the decreasing width sequence resulting in the max height
    # you can sort by width if you so wish

    boxes.sort(reverse=True)
    sums: list[int] = [box[2] for box in boxes]

    for i in range(1, len(boxes)):
        subproblems: list[int] = [
            sums[k]
            for k in range(i)
            if boxes[k][0] > boxes[i][0] and boxes[k][1] > boxes[i][1]
        ]
        sums[i] = max(subproblems, default=0) + boxes[i][2]

    return max(sums)


if __name__ == "__main__":
    boxes = [
        (2, 4, 1),
        (1, 2, 2),
        (2, 3, 2),
        (3, 6, 2),
        (1, 5, 4),
        (4, 5, 3),
        (2, 3, 2),
    ]

    boxes = [
        (5, 2, 1),
        (2, 5, 3),
        (4, 5, 1),
        (3, 4, 1),
        (2, 1, 2),
        (4, 1, 2),
        (5, 3, 3),
        (4, 1, 5),
        (2, 2, 4),
    ]
    print(find_max_height_stacked_boxes(boxes))
