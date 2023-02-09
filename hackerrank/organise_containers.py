import itertools


def organizingContainers(containers):
    # Write your code here
    no_of_containers = len(containers)

    # note: number of ball types equals number of containers
    # note: containers have a 'fixed' capacity due to only swaps allowed
    container_capacities = [0] * no_of_containers
    ball_types_count = [0] * no_of_containers

    for container, ball_type in itertools.product(
        range(no_of_containers), range(no_of_containers)
    ):
        # to find the capacities of each sub-container
        container_capacities[container] += containers[container][ball_type]
        # to find the number of balls of a certain ball type
        ball_types_count[container] += containers[ball_type][container]

    # a container can store any ball type, therefore sorting the two and comparing shows that
    # there exists a container than can carry all balls of a certain ball type
    if sorted(container_capacities) == sorted(ball_types_count):
        return "Possible"

    return "Impossible"


print(
    organizingContainers(
        [
            [999013654, 998634077, 997988323, 958769423],  # 0
            [997409523, 999301350, 940952923, 993020546],  # 1
            [960369681, 997828120, 999792735, 979622676],  # 2
            [997612619, 934920795, 998879231, 999926463],  # 3
        ]
    )
)

print(organizingContainers([[2, 0, 0], [0, 2, 1], [1, 1, 1]]))
