# Technique: Linked list iteration / simultaneous comparison with next node
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def dedup_sorted_list(head: Node) -> Node:

    current_node = head

    while current_node is not None and current_node.next is not None:
        
        if current_node.value == current_node.next.value:
            current_node.next = current_node.next.next
        else:
            
            current_node = current_node.next

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
    """Helper function to convert a linked list into a Python list."""
    values = []
    current_node = head

    while current_node is not None:
        values.append(current_node.value)
        current_node = current_node.next

    return values


def run_tests() -> None:
    # example style cases
    head_one = build_linked_list([1, 1, 2, 3, 3])
    updated_head_one = dedup_sorted_list(head_one)
    assert linked_list_to_list(updated_head_one) == [1, 2, 3]

    head_two = build_linked_list([1, 1, 1, 1])
    updated_head_two = dedup_sorted_list(head_two)
    assert linked_list_to_list(updated_head_two) == [1]

    head_three = build_linked_list([1, 2, 3, 4])
    updated_head_three = dedup_sorted_list(head_three)
    assert linked_list_to_list(updated_head_three) == [1, 2, 3, 4]

    # edge cases
    empty_head = build_linked_list([])
    updated_empty_head = dedup_sorted_list(empty_head)
    assert linked_list_to_list(updated_empty_head) == []

    single_head = build_linked_list([5])
    updated_single_head = dedup_sorted_list(single_head)
    assert linked_list_to_list(updated_single_head) == [5]

    head_four = build_linked_list([0, 0, 1, 1, 1, 2, 3, 3])
    updated_head_four = dedup_sorted_list(head_four)
    assert linked_list_to_list(updated_head_four) == [0, 1, 2, 3]

    print("All tests passed")


if __name__ == "__main__":
    run_tests()