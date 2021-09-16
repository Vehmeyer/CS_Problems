"""
You are given a binary tree. Write a function that returns the binary tree's node values using an in-order traversal.
"""

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def binaryTreeInOrderTraversal(root):
    result = []
    helper(root, result)
    return result
    
def helper(root, result):
    if root is None:
        return
    
    helper(root.left, result)
    result.append(root.value)
    helper(root.right, result)

"""
Note: Try to solve this task without using recursion, since this is what you'll be asked to do during an interview.

Given a binary tree of integers t, return its node values in the following format:

The first element should be the value of the tree root;
The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
Etc.
"""

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):
    if t is None:
        return []
        
    result = []
    queue = []
    queue.append(t)
    
    while len(queue) != 0:
        node = queue.pop(0)
        result.append(node.value)
        
        if node.left is not None:
            queue.append(node.left)
            
        if node.right is not None:
            queue.append(node.right)
    
    return result

"""
Given a binary tree of integers, return all the paths from the tree's root to its leaves as an array of strings. 
The strings should have the following format:
"root->node1->node2->...->noden", representing the path from root to noden, where root is the value stored in the root 
and node1,node2,...,noden are the values stored in the 1st, 2nd,..., and nth nodes in the path respectively (noden representing the leaf).
"""

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def treePaths(t):
    paths = []
    
    def helper(t, current):
        if t is None:
            return 
        if t.left is None and t.right is None:
            current += str(t.value)
            paths.append(current)
        else:
            current += str(t.value) + "->"
        
        helper(t.left, current)
        helper(t.right, current)
        
    helper(t, "")
    
    return paths
#