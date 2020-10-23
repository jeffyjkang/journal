# Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
# Example:
# Input: 1 -> 2 -> 4, 1 -> 3 -> 4
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

# create node class
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# create function that merges two singly linked lists
def merge_two_lists(l_1, l_2):
    # initialize a dummy_head for the return linked list
    dummy_head = Node(0)
    # initialize the current pointer to the dummy head
    current_pointer = dummy_head
    # loop while linked list 1 and linked list 2 is not None
    while l_1 != None and l_2 != None:
        # if the value of the current node in linked list 1 is less than or equal to the value of the current node in linked list 2
        if l_1.value <= l_2.value:
            # assign the current pointer's next value to linked list 1's current node
            current_pointer.next = l_1
            # reassign linked list 1 to linked list 1's next node
            l_1 = l_1.next
        # if the value of the current node in linked list 1 is greater than the value of the current node in linked list 2
        else:
            # assign the current pointer's next value to linked list 2's current node
            current_pointer.next = l_2
            # reassign linked list 2 to linked list 2's next node
            l_2 = l_2.next
        # reassign the current pointer to current pointer's next node
        current_pointer = current_pointer.next
    # at the end of the loop if linked list 2 is None, assign current pointer's next value to linked list 1, else linked list 2
    current_pointer.next = l_1 if l_2 == None else l_2
    # return the merged linked list, minus the dummy head
    return dummy_head.next

# initializing linked list 1 and linked list 2
linked_list_1 = Node(1)
linked_list_1.next = Node(2)
linked_list_1.next.next = Node(4)
linked_list_2 = Node(1)
linked_list_2.next = Node(3)
linked_list_2.next.next = Node(4)

merged_list = merge_two_lists(linked_list_1, linked_list_2)

while merged_list != None:
    print(merged_list.value)
    merged_list = merged_list.next

TAGS = ['LINKED_LIST', 'SINGLY_LINKED_LIST', 'MERGE']