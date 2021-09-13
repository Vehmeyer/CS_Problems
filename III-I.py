#Note: Your solution should have O(n) time complexity, where n is the number of elements in l,
#since this is what you will be asked to accomplish in an interview.
#You have a singly linked list l, which is sorted in strictly increasing order, and an integer value. 
#Add value to the list l, preserving its original sorting.
#Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: 
#in real data you will be given a head node l of the linked list

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def insertValueIntoSortedLinkedList(l, value):
    new_node = ListNode(value)
    current = l
    
    if l == None:
        return new_node
    if new_node.value < current.value:
        new_node.next = current
        return new_node
    while current.next is not None:
        if current.next.value > new_node.value:
            new_node.next = current.next
            current.next = new_node
            return l
        current = current.next
    current.next = new_node
    return l

#Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.
#Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, 
#also sorted in non-decreasing order, that contains the elements from both original lists.

