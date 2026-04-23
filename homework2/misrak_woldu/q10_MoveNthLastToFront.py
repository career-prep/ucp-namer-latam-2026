# Technique: Fixed-distance two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def move_nth_last_to_front(head: Node, n: int) -> Node:

    if head is None or n <= 0:
        return head

    lead_pointer = head

    for _ in range(n - 1):
        if lead_pointer.next is None:
            return head
        lead_pointer = lead_pointer.next

    if lead_pointer is None:
        return head

    trailing_pointer = head
    node_before_target = None

    while lead_pointer.next is not None:
        lead_pointer = lead_pointer.next
        node_before_target = trailing_pointer
        trailing_pointer = trailing_pointer.next

    target_node = trailing_pointer

    if target_node == head:
        return head

    node_before_target.next = target_node.next

    target_node.next = head

    return target_node


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
    head_one = build_linked_list([1, 2, 3, 4, 5])
    updated_head_one = move_nth_last_to_front(head_one, 2)
    assert linked_list_to_list(updated_head_one) == [4, 1, 2, 3, 5]

    head_two = build_linked_list([1, 2, 3, 4, 5])
    updated_head_two = move_nth_last_to_front(head_two, 1)
    assert linked_list_to_list(updated_head_two) == [5, 1, 2, 3, 4]

    head_three = build_linked_list([1, 2, 3, 4, 5])
    updated_head_three = move_nth_last_to_front(head_three, 5)
    assert linked_list_to_list(updated_head_three) == [1, 2, 3, 4, 5]

    head_four = build_linked_list([10])
    updated_head_four = move_nth_last_to_front(head_four, 1)
    assert linked_list_to_list(updated_head_four) == [10]

    head_five = build_linked_list([1, 2, 3])
    updated_head_five = move_nth_last_to_front(head_five, 4)
    assert linked_list_to_list(updated_head_five) == [1, 2, 3]

    head_six = build_linked_list([1, 2, 3])
    updated_head_six = move_nth_last_to_front(head_six, 0)
    assert linked_list_to_list(updated_head_six) == [1, 2, 3]

    updated_head_seven = move_nth_last_to_front(build_linked_list([1, 2, 3]), -1)
    assert linked_list_to_list(updated_head_seven) == [1, 2, 3]

    assert move_nth_last_to_front(None, 1) is None

    print("All tests passed")


if __name__ == "__main__":
    run_tests()