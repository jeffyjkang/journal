# Swap Nodes In Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
# Example:
# Given 1 -> 2 -> 3 -> 4, you should return the list as  2 -> 1 -> 4 -> 3.
# Note:
# Your algorithm should use only constatnt extra space.
# You may not modify the values in the lists's nodes, only nodes itself may be changed.

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
head.next.next.next.next.next = Node(6)

def swap_pairs(h):
    # initialize a dummy head and current pointer to a Node with an arbitrary value
    dummy = current = Node(0)
    # assign dummy's next node to the head node passed into the function
    dummy.next = h
    # iterate while current, current's next node and current's next, next node is not None
    while current and current.next and current.next.next:
        # looking ahead, initialize a first pointer to current's next node, and initialize a second pointer to current's next, next node
        first = current.next; second = current.next.next
        # reassign first's next node to second's next node
        first.next = second.next
        # reassign second's next node to first
        second.next = first
        # reassign current's next node to second
        current.next = second
        # reassign current' pointer to current's next, next node
        current = current.next.next
    # return dummy's next node which would be the swapped linked list's head
    return dummy.next

swapped_linked_list = swap_pairs(head)

def print_linked_list(h):
    while h:
        print(h.value)
        h = h.next

print_linked_list(swapped_linked_list)

TAGS = ['LINKED_LIST', 'SINGLY_LINKED_LIST', 'SWAP']
