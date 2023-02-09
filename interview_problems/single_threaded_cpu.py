import heapq


def single_threaded_cpu(tasks: list[list[int]]) -> list[int]:
    """
    single_threaded_cpu
    You are given n tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei]
    means that the ith task will be available to process at enqueueTimei and will take processingTimei to finish processing.

    You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

    - If the CPU is idle and there are no available tasks to process, the CPU remains idle.
    - If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time.
      If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
    - Once a task is started, the CPU will process the entire task without stopping.
    - The CPU can finish a task then start a new one instantly.

    Return the order in which the CPU will process the tasks.

    Args:
        tasks (list[list[int]]): 2D array of CPU tasks

    Returns:
        list[int]: order in which tasks were executed
    """

    tasks_in_order: list[int] = []
    priority_queue: list[list[int]] = []
    no_of_tasks: int = len(tasks)
    tasks.sort()

    current_time: int = 0
    current_task: int = 0
    added = False

    for idx, task in enumerate(tasks):
        task.append(idx)

    while current_task < no_of_tasks or priority_queue:
        for enq_time, proc_time, task_idx in tasks[current_task:]:
            if enq_time <= current_time:
                added = True
                heapq.heappush(priority_queue, [proc_time, task_idx])
                current_task += 1
            else:
                if not added:
                    current_time += 1
                added = False
                break

        print(priority_queue)

        if priority_queue:
            proc_time, task_idx = heapq.heappop(priority_queue)
            current_time += proc_time
            print(current_time)
            tasks_in_order.append(task_idx)

    return tasks_in_order


if __name__ == "__main__":
    print(single_threaded_cpu([[1, 2], [2, 4], [3, 2], [4, 1]]))
