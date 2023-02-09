# LINKED LISTS

# an ordered, zero-indexed data structure made up of nodes
# each node stores data (strings, lists, objects, etc) and
# a pointer to the next node in the linked list

# nodes are not stored contiguously in memory, unlike arrays
# example advantage: for an insertion operation, linked lists have O(1)
# whereas arrays have O(n) due to how the operation is implemented at a low level

# to traverse a linked list, all you need to have is a pointer to the head node
# as you can access the entire linked lists from it through nodes and pointers
# therefore, a reference to the head node is always kept

from string import ascii_lowercase
from typing import Any, Optional


# creating the nodes that comprise the linked list
class Node:
    def __init__(
        self, stored_value: Any, pointer_to_next_node: Optional[Any] = None
    ) -> None:
        self.stored_value = stored_value
        self.pointer_to_next_node = pointer_to_next_node


# to create the actual linked list
class LinkedList:
    def __init__(self) -> None:
        """Initialises the linked list with an empty head node"""

        self.head_node = None

    def append(self, node_value: Any) -> None:
        """Appends values to the end of the linked list
        (starting from the head if the linked list is empty)"""

        if self.head_node is None:
            self.head_node = Node(node_value)
            return

        self.append_helper(node_value, self.head_node)

    def append_helper(self, node_value: Any, current_node: Node) -> None:
        """Recursive helper function for append operation"""
        # the helper function also alleviates the need to pass the head node explicitly
        # as an argument in the parent function call

        if current_node.pointer_to_next_node is None:
            current_node.pointer_to_next_node = Node(node_value)
            return

        self.append_helper(node_value, current_node.pointer_to_next_node)

    def print_list(self):
        """Prints the values of the linked list"""

        printed_list: str = self.print_list_helper(self.head_node)
        print(printed_list)

    def print_list_helper(self, current_node: Node) -> str:
        """Recursive helper function for the print operation"""
        # the helper function also alleviates the need to pass the head node explicitly
        # as an argument in the parent function call

        return (
            "None"
            if current_node is None
            else f"{str(current_node.stored_value)} -> {self.print_list_helper(current_node.pointer_to_next_node)}"
        )

    def contains(self, node_value: Any) -> bool:
        """Traverses the linked list, searching for a given input value.
        If the value is absent, returns None"""

        if is_contained := self.contains_helper(node_value, self.head_node):
            print(f"{node_value} is present in linked list.")
            return True
        print(f"{node_value} is not in linked list.")
        return False

    def contains_helper(self, node_value: Any, current_node: Node):
        """Recursive helper function for the contains operation"""
        # the helper function also alleviates the need to pass the head node explicitly
        # as an argument in the parent function call

        if current_node is None:
            return
        if current_node.stored_value == node_value:
            return True
        return self.contains_helper(node_value, current_node.pointer_to_next_node)

    def retrieve(self, node_index: int) -> Any:
        """Retrieves the value stored in the linked list at a given input node index.
        If input node index is out of range, returns None"""

        return self.retrieve_helper(self.head_node, node_index)

    def retrieve_helper(self, current_node: Node, node_index: int) -> Any:
        """Recursive helper function for retrieve operation"""
        # the helper function also alleviates the need to pass the head node explicitly
        # as an argument in the parent function call

        if current_node is None:
            return "Node index is out of range."
        if node_index == 0:
            return current_node.stored_value
        return self.retrieve_helper(current_node.pointer_to_next_node, node_index - 1)


def sum_linked_list_iteratively(head_node: Node) -> None:
    """Iteratively traverses the linked list,
    storing values at each node into a list stored_values.
    Also finds sum of elements"""

    current_node: Node = head_node
    sum_of_linked_list = 0

    # while the value of the current_node node being checked is not None
    while current_node != None:
        current_node_value = current_node.stored_value
        sum_of_linked_list += current_node_value
        current_node = current_node.pointer_to_next_node

    print(sum_of_linked_list)


# to traverse the linked list recursively
def sum_linked_list_recursively(head_node: Node) -> int:
    """Recursively traverses the linked list,
    storing values at each node into a list stored_values.
    Also finds sum of elements"""

    current_node: Node = head_node

    # DEFINE A BASE CASE
    # base case is achieved when the current_node value is none
    # indicating that we are at the end of the linked list
    if current_node is None:
        return 0

    # DEFINE THE LEAST AMOUNT OF WORK TO BE DONE
    # for this case, least amount is to keep traversing down the linked list,
    # one node at a time until the end is reached
    return current_node.stored_value + sum_linked_list_recursively(
        current_node.pointer_to_next_node
    )


def delete_value(
    linked_list: LinkedList,
    head_node: Node,
    value_to_delete: Any,
    previous_node: Optional[Node] = None,
):
    """Deletes an input value from the linked list, if the value is present.
    Then prints out the resultant linked list.
    If absent, returns None."""

    current_node: Node = head_node

    if previous_node is None and current_node.stored_value == value_to_delete:
        # if the value to be deleted is stored in the head node
        # set the linked list's head node to be the next node
        linked_list.head_node = current_node.pointer_to_next_node
        linked_list.print_list()
        return

    if current_node is None:
        # if the whole linked list has been traversed and the value has not been found]
        linked_list.print_list()
        return "Value not found."

    if current_node.stored_value == value_to_delete:
        # deletion is achieved by rerouting the linked list or bypassing the current node i.e.
        # setting the previous node's pointer to point to the next node instead of the current node
        previous_node.pointer_to_next_node = current_node.pointer_to_next_node
        print(f"Deleted {value_to_delete} from the linked list")
        linked_list.print_list()
        return

    previous_node = current_node
    current_node = current_node.pointer_to_next_node

    return delete_value(linked_list, current_node, value_to_delete, previous_node)


def reverse_linked_list(
    linked_list: LinkedList, head_node: Node, previous_node: Optional[Node] = None
) -> Node:
    """Recursively reverses a linked list"""

    current_node: Node = head_node

    if current_node is None:
        linked_list.head_node = previous_node
        linked_list.print_list()
        return linked_list.head_node

    # using a temporary variable next_node to keep track of the (pointer to the) next node
    # before reassigning current_node's next pointer to point to the previous node
    next_node: Node = current_node.pointer_to_next_node

    current_node.pointer_to_next_node = previous_node
    previous_node = current_node
    current_node = next_node

    return reverse_linked_list(linked_list, current_node, previous_node)


def zip_linked_lists_iteratively(first_head_node: Node, second_head_node: Node) -> Node:
    """Iteratively zips two linked lists, like the zip() function"""

    node_counter: int = 0
    tail_node: Node = first_head_node
    current_node_1: Node = first_head_node.pointer_to_next_node
    current_node_2: Node = second_head_node

    while current_node_1 != None and current_node_2 != None:
        if node_counter % 2 == 0:
            tail_node.pointer_to_next_node = current_node_2
            current_node_2 = current_node_2.pointer_to_next_node
        else:
            tail_node.pointer_to_next_node = current_node_1
            current_node_1 = current_node_1.pointer_to_next_node

        tail_node = tail_node.pointer_to_next_node
        node_counter += 1

    if current_node_1 != None:
        tail_node.pointer_to_next_node = current_node_1
    if current_node_2 != None:
        tail_node.pointer_to_next_node = current_node_2

    return first_head_node


def zip_linked_lists_recursively(first_head_node: Node, second_head_node: Node) -> Node:
    """Recursively zips two linked lists, like the zip() function"""

    if first_head_node is None:
        return None if second_head_node is None else second_head_node
    if second_head_node is None:
        return first_head_node

    next_node_1: Node = first_head_node.pointer_to_next_node
    next_node_2: Node = second_head_node.pointer_to_next_node
    first_head_node.pointer_to_next_node = second_head_node
    second_head_node.pointer_to_next_node = zip_linked_lists_recursively(
        next_node_1, next_node_2
    )
    return first_head_node


# linked list structure:
# A -> B -> C -> D -> None

new_linked_list = LinkedList()

for value in range(1, 21):
    new_linked_list.append(value)

first_node: Node = new_linked_list.head_node

new_linked_list.print_list()

# sum_linked_list_iteratively(first_node)
sum_of_input_list: int = sum_linked_list_recursively(first_node)
print(sum_of_input_list)

search_value: Any = 3
new_linked_list.contains(search_value)


input_node_index: int = 9
input_node_value: Any = new_linked_list.retrieve(node_index=input_node_index)

print(input_node_value)

delete_value(new_linked_list, first_node, 3)

search_value: Any = 3
new_linked_list.contains(search_value)

new_list_head_node = reverse_linked_list(new_linked_list, first_node)

if new_list_head_node is None:
    print("Empty linked list.")
else:
    print(new_list_head_node.stored_value)

first_linked_list = LinkedList()
second_linked_list = LinkedList()

for i in range(10, 21):
    first_linked_list.append(i)

for i in ascii_lowercase:
    second_linked_list.append(i)

# zipped_linked_list: Node = zip_linked_lists_iteratively(
#     first_linked_list.head_node, second_linked_list.head_node
# )
zipped_linked_list: Node = zip_linked_lists_recursively(
    first_linked_list.head_node, second_linked_list.head_node
)

first_linked_list.print_list()
