def can_finish(num_courses: int, prerequisites: list[int]) -> bool:
    """
    can_finish checks whether it is possible to complete all courses in a course list given each course's prerequisites

    Args:
        num_courses (int): total number of available courses
        prerequisites (list[int]): each course and its prerequisite pair

    Returns:
        bool: possible to finish all course or not
    """

    # adjacency list
    prerequisites_map = {i: [] for i in range(num_courses)}
    for course, prerequisite in prerequisites:
        prerequisites_map[course].append(prerequisite)

    # prevent CYCLES
    visited = set()

    def depth_first_search(course: int) -> bool:
        if course in visited:
            return False
        if prerequisites_map[course] == []:
            return True

        visited.add(course)

        for prereq in prerequisites_map[course]:
            if not depth_first_search(prereq):
                return False
        visited.remove(course)
        prerequisites_map[course] = []
        return True

    for crs in range(num_courses):
        if not depth_first_search(crs):
            return False

    return True


print(can_finish(5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]))
print(can_finish(3, [[0, 1], [1, 2], [2, 0]]))
