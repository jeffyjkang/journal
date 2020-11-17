# Merge K Sorted Lists
# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.
# Example:
# Input:
# [
#     1 -> 4 -> 5,
#     1 -> 3 -> 4,
#     2 -> 6
# ]
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

# create node class
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# initialize the three linked lists to put in the list
l_l_1 = Node(1)
l_l_1.next = Node(4)
l_l_1.next.next = Node(5)
l_l_2 = Node(1)
l_l_2.next = Node(3)
l_l_2.next.next = Node(4)
l_l_3 = Node(2)
l_l_3.next = Node(6)

# initialize list of linked list
l_l_l = [l_l_1, l_l_2, l_l_3]

# function that takes in a list of linked list and merges them
def merge_k_lists(lists):
    # assign amount to the length of the list of linked lists
    amount = len(lists)
    # initialize interval to 1
    interval = 1
    # iterate while interval is less than amount
    while interval < amount:
        # loop through the indices where start is 0, stop is amount minus interval, and the step is the product of interval and 2
        for i in range(0, amount - interval, interval * 2):
            # assign the list of linked lists index of 0 to the result of calling merge_2_lists passing in lists at index of i and lists at index i plus interval
            lists[i] = merge_2_lists(lists[i], lists[i + interval])
        # after the completion of the for loop, reassign interval to the product of itself and 2
        interval *= 2
    # return the now merged list which would be the 0th index of lists if the list was not empty, else None
    return lists[0] if amount > 0 else None

# helper function to merge two linked lists
def merge_2_lists(list_1, list_2):
    # initialize dummy head and pointer to a node with arbitrary value of 0
    head = point = Node(0)
    # iterate while list 1 and list 2 are not None
    while list_1 and list_2:
        # if the value of list 1's current node is less than or equal to the value of list 2's current node
        if list_1.value <= list_2.value:
            # assign current pointer's next value to list 1's current node
            point.next = list_1
            # reassign list 1's current node to its next node
            list_1 = list_1.next
        # if the value of list 1's current node is greater than the value of list 2's current node
        else:
            # assign current pointer's next value to list 2's current node
            point.next = list_2
            # reassign list 2's current node to its next node
            list_2 = list_2.next
        # reassign the current pointer to current pointer's next node
        point = point.next
    # at the end of the loop if linked list 1 is None, assign current pointer's next value to linked list 2, else linked list 1
    point.next = list_2 if list_1 == None else list_1
    # return the dummy head's next node
    return head.next

merged_linked_list = merge_k_lists(l_l_l)

def print_linked_list(head):
    while head:
        print(head.value)
        head = head.next

print_linked_list(merged_linked_list)

TAGS = ['LINKED_LIST', 'SINGLY_LINKED_LIST', 'MERGE']
