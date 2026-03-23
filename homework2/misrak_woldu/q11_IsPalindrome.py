# Technique: Fast/slow pointers + reverse second half
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def is_palindrome(head: Node) -> bool:

    if head is None or head.next is None:
        return True

    # Find the middle of the list
    slow_pointer = head
    fast_pointer = head

    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    # If the list has odd length skip the middle node
    if fast_pointer is not None:
        slow_pointer = slow_pointer.next

    # Reverse the second half of the list
    reversed_second_half_head = reverse_list(slow_pointer)

    # Compare first half and reversed second half
    first_half_pointer = head
    second_half_pointer = reversed_second_half_head

    while second_half_pointer is not None:
        if first_half_pointer.value != second_half_pointer.value:
            return False

        first_half_pointer = first_half_pointer.next
        second_half_pointer = second_half_pointer.next

    return True

def reverse_list(head: Node) -> Node:
    
    previous_node = None
    current_node = head

    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node


def build_linked_list(values: list[int]) -> Node:
    """Helper to build a linked list from a Python list."""
    if not values:
        return None

    head = Node(values[0])
    current_node = head

    for value in values[1:]:
        current_node.next = Node(value)
        current_node = current_node.next

    return head


def run_tests() -> None:
    # even length palindrome
    head_one = build_linked_list([1, 2, 2, 1])
    assert is_palindrome(head_one) is True

    # odd length palindrome
    head_two = build_linked_list([1, 2, 3, 2, 1])
    assert is_palindrome(head_two) is True

    # not a palindrome
    head_three = build_linked_list([1, 2, 3, 4])
    assert is_palindrome(head_three) is False

    # single node
    head_four = build_linked_list([5])
    assert is_palindrome(head_four) is True

    # empty list
    assert is_palindrome(None) is True

    # two nodes
    head_five = build_linked_list([7, 7])
    assert is_palindrome(head_five) is True

    head_six = build_linked_list([7, 8])
    assert is_palindrome(head_six) is False

    # longer palindrome
    head_seven = build_linked_list([9, 1, 2, 3, 2, 1, 9])
    assert is_palindrome(head_seven) is True

    print("All tests passed")


if __name__ == "__main__":
    run_tests()