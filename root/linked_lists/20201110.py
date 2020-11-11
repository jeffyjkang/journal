# Reverse Nodes In K-Group
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# Example:
# Given a linked list: 1 -> 2 -> 3 -> 4 -> 5
# for k = 2, you should return 2 -> 1 -> 4 -> 3 -> 5
# for k = 3, you should return 3 -> 2 -> 1 -> 4 -> 5
# Note:
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.

# create node class
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# initialize the linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

def reverse_by_k(head, k):
    # initialize current pointer to the passed in head node
    current = head
    # initialize count to 0
    count = 0
    # loop while current is not empty and count is less than k
    while current and count < k:
        # reassign the current pointer to the current pointer's next node
        current = current.next
        # increment count by 1
        count += 1
    # if count is less than k, it would mean the count of the remaining nodes is greater than k
    if count < k:
        # return the passed in head node
        return head
    # assign new head to the return value of the recursive call of reverse_by_k, passing in the current pointer and k
    new_head = reverse_by_k(current, k)
    # iterate while count is greater than 0
    while count > 0:
        # initialize a next pointer to the head's next node
        next = head.next
        # reassign the head's next node to new_head
        head.next = new_head
        # reassign new_head to head
        new_head = head
        # reassign head to next
        head = next
        # decrement count by 1
        count -= 1
    # return new_head
    return new_head

reversed_by_k = reverse_by_k(head, 2)

def print_linked_list(node):
    while node:
        print(node.value)
        node = node.next

print_linked_list(reversed_by_k)

TAGS = ['LINKED_LIST', 'SINGLY_LINKED_LIST', 'REVERSE', 'RECURSION']