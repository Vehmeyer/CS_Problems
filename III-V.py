"""
Note: Your solution should have O(l.length) time complexity and O(1) space complexity, since this is what you will be asked 
to accomplish in an interview.

Given a singly linked list, reverse and return it.
"""

def reverseLinkedList(l):
    prev = None
    curr = l
    
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev

"""
You are given the root node of a binary search tree (BST).

You need to write a function that returns the sum of values of all the nodes with a value between lower and upper (inclusive).

The BST is guaranteed to have unique values.
"""

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBSTRangeSum(root, lower, upper):
    sum = 0
    
    def helper(root, lower, upper):
        nonlocal sum
        if not root:
            return 0
        if root.value >= lower and root.value <= upper:
            sum += root.value
        if root.value >= lower:
            helper(root.left, lower, upper)
        if root.value <= upper:
            helper(root.right, lower, upper)
    
    helper(root, lower, upper)
    return sum

"""
Given a binary tree, write a function that inverts the tree.
"""

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBinaryTreeInvert(root):
    if root is None:
        return
    swapNodes(root)
    csBinaryTreeInvert(root.left)
    csBinaryTreeInvert(root.right)
    return root
    
def swapNodes(root):
    root.left, root.right = root.right, root.left
