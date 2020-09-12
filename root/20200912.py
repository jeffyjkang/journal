# Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807

# create node class
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# create a function that takes a list of numbers and initializes the linked list
def init_linked_list(nums):
    # initialize a root variable by assigning a null value
    root = None
    # loop through the indices of numbers
    for i in range(len(nums)):
        # create a temp variable to hold the current node
        temp = Node(nums[i])
        # assign root node if value is null value
        if root == None:
            root = temp
        # continue if root node has already been assigned
        else:
            # initialize pointer variable to root node
            pointer = root
            # if the pointer node's next value is not null, traverse the linked list to the next node while assigning the pointer to the next node
            while pointer.next != None:
                pointer = pointer.next
            # when the pointer node's next value is null, assign the pointer node's next value to the current Node in the loop
            pointer.next = temp
    # return the linked list
    return root

# function to add two numbers
def add_two_numbers(nums1, nums2):
    # initialize sum root node's value to 0, note: sum_root node is dummy head
    sum_root = Node(0)
    # initialize pointer to first node in first linked list
    pointer1 = nums1
    # initialize pointer to first node in second linked list
    pointer2 = nums2
    # initialize current pointer to the sum root node
    current_pointer = sum_root
    # initialize carry value to 0
    carry = 0
    # loop through both linked lists simultaneously
    while pointer1 != None or pointer2 != None:
        # get the int value of nums1 node or 0 if no node
        int1 = pointer1.value if pointer1 != None else 0
        # get the int value of nums2 node or 0 if no node
        int2 = pointer2.value if pointer2 != None else 0
        # get sum of node 1 value, node 2 value and the carry if available
        int_sum = carry + int1 + int2
        # assign carry as the 10's place value will be either 1 or 0
        carry = int(int_sum / 10)
        # assign the current pointer's next node to be the ones place of the int sum
        current_pointer.next = Node(int_sum % 10)
        # assign the current pointer to the next node
        current_pointer = current_pointer.next
        # if pointer1 exists assign it to the next node
        if pointer1 != None:
            pointer1 = pointer1.next
        # if pointer2 exists assign it to the next node
        if pointer2 != None:
            pointer2 = pointer2.next
    # after the loop, if carry exists create final node with the carry as the value
    if carry > 0:
        current_pointer.next = Node(carry)
    # return sum_root's next node, due to the sum_root node being a dummy head
    return sum_root.next

def read_linked_list(singly_linked_list):
    # assign current pointer to root node of the singly linked list
    current_pointer = singly_linked_list
    # while current pointer exists loop through the linked list
    while current_pointer:
        # print value of current node
        print(current_pointer.value)
        # reassign current pointer to the next node
        current_pointer = current_pointer.next

first_nums = [2, 4, 3]
second_nums = [5, 6, 4]

first_linked_list = init_linked_list(first_nums)
second_linked_list = init_linked_list(second_nums)
sum_linked_list = add_two_numbers(first_linked_list, second_linked_list)
read_linked_list(sum_linked_list)
