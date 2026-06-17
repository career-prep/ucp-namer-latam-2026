# Technique: Fast/slow pointers + reset/catch-up
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def disconnect_cycle(head: Node) -> Node:
    
    if head is None or head.next is None:
        return head

    slow_pointer = head
    fast_pointer = head
    meeting_node = None

    # Detect whether a cycle exists
    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            meeting_node = slow_pointer
            break

    if meeting_node is None:
        return head

    # Find the start of the cycle
    pointer_from_head = head
    pointer_from_meeting = meeting_node

    while pointer_from_head != pointer_from_meeting:
        pointer_from_head = pointer_from_head.next
        pointer_from_meeting = pointer_from_meeting.next

    cycle_start = pointer_from_head

    # Find the node right before the cycle start
    cycle_end = cycle_start
    while cycle_end.next != cycle_start:
        cycle_end = cycle_end.next

    # Break the cycle
    cycle_end.next = None

    return head

def build_linked_list(values: list[int]) -> Node:

    if not values:
        return None

    head = Node(values[0])
    current_node = head

    for value in values[1:]:
        current_node.next = Node(value)
        current_node = current_node.next

    return head


def linked_list_to_list(head: Node) -> list[int]:
    
    values = []
    current_node = head

    while current_node is not None:
        values.append(current_node.value)
        current_node = current_node.next

    return values


def run_tests() -> None:
    # empty list
    assert disconnect_cycle(None) is None

    # single node without cycle
    single_node = Node(10)
    updated_single_node = disconnect_cycle(single_node)
    assert linked_list_to_list(updated_single_node) == [10]

    # list without cycle
    regular_head = build_linked_list([1, 2, 3, 4, 5])
    updated_regular_head = disconnect_cycle(regular_head)
    assert linked_list_to_list(updated_regular_head) == [1, 2, 3, 4, 5]

    # cycle starting in the middle
    head_one = build_linked_list([1, 2, 3, 4, 5])
    cycle_start_one = head_one.next.next          # node with value 3
    tail_one = cycle_start_one.next.next          # node with value 5
    tail_one.next = cycle_start_one

    updated_head_one = disconnect_cycle(head_one)
    assert linked_list_to_list(updated_head_one) == [1, 2, 3, 4, 5]

    # cycle starting at head
    head_two = build_linked_list([1, 2, 3, 4])
    tail_two = head_two.next.next.next            # node with value 4
    tail_two.next = head_two

    updated_head_two = disconnect_cycle(head_two)
    assert linked_list_to_list(updated_head_two) == [1, 2, 3, 4]

    # single node with cycle to itself
    self_cycle_node = Node(99)
    self_cycle_node.next = self_cycle_node

    updated_self_cycle_node = disconnect_cycle(self_cycle_node)
    assert linked_list_to_list(updated_self_cycle_node) == [99]

    print("All tests passed")


if __name__ == "__main__":
    run_tests()