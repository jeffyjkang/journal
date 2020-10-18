# Remove Nth Node From End Of List
# Given a linked list, remove the n-th node from the end of list and return its head.
# Example:
# Given linked list: 1 -> 2 -> 3 -> 4 -> 5, and n = 2.
# After removing the second node from the end, the linked list becomes 1 -> 2 -> 3 -> 5.
# Note:
# Given n will always be valid.
# Follow up:
# Could you do this in one pass?

# create node class
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# create function that takes a list of numbers and initializes a linked list
def init_linked_list(nums):
    # initialize root node to null value
    root = None
    # loop through the indices of numbers
    for i in range(len(nums)):
        # create a temp variable and assign it to an instantiated node with the current index's value
        temp = Node(nums[i])
        # only applies to first instance when root node is null, assign it to temp
        if root == None: root = temp
        # if a root node exists
        else:
            # initialize pointer variable to root node
            pointer = root
            # if the pointer node's next value is not null, traverse the linked list to the next node while assigning the pointer to the next node
            while pointer.next != None:
                pointer = pointer.next
            # when pointer.next is not none, assign pointer's next value to the temp node
            pointer.next = temp
    # return the root node of the linked list
    return root

# function to remove nth node from the end of a linked list
def remove_nth_from_end(head, from_end):
    # initialize first pointer and second pointer to head of linked list
    first = head; second = head
    # advance first pointer, so there is a gap between the first and second pointers, by assigning first pointer to first.next
    for _ in range(from_end):
        first = first.next
    # if first pointer is None, it means it was the last node from head
    if first == None:
        # will return with head node removed, or None if linked list was one node
        return head.next
    # advance the first pointer once more so that the gap is appropriate when removing the nth node
    first = first.next
    # while first pointer is not None
    while first:
        # assign first pointer to first.next and second pointer to second.next
        first = first.next; second = second.next
    # remove node by assigning second.next to second.next.next
    second.next = second.next.next
    # return head node
    return head

n = [1, 2, 3, 4, 5]

head_node = init_linked_list(n)
target_from_end = 2
new_linked_list = remove_nth_from_end(head_node, target_from_end)

while new_linked_list:
    print(new_linked_list.value)
    new_linked_list = new_linked_list.next

TAGS = ['LINKED_LIST', 'SINGLY_LINKED_LIST', 'REMOVE']
