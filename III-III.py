"""
You are given a binary tree and you need to write a function that can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node differ in height by a maximum of 1.
"""

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

class TreeDetails:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height

def balancedBinaryTree(root):
    TreeDetails = getTreeDetails(root)
    return TreeDetails.isBalanced
    
def getTreeDetails(node):
    if node == None:
        return TreeDetails(True, -1)
        
    leftSubtreeInfo = getTreeDetails(node.left)
    rightSubtreeInfo = getTreeDetails(node.right)
    
    isBalanced = leftSubtreeInfo.isBalanced and rightSubtreeInfo.isBalanced and abs(leftSubtreeInfo.height - rightSubtreeInfo.height) <= 1
    height = max(leftSubtreeInfo.height, rightSubtreeInfo.height) + 1
    return TreeDetails(isBalanced, height)

"""
You are given a binary tree and you are asked to write a function that finds its minimum depth. The minimum depth can be defined as the 
number of nodes along the shortest path from the root down to the nearest leaf node. As a reminder, a leaf node is a node with no children.
"""

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def minimumDepthBinaryTree(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return minimumDepthBinaryTree(root.right) + 1
    if root.right is None:
        return minimumDepthBinaryTree(root.left) + 1  
    return min(minimumDepthBinaryTree(root.left), minimumDepthBinaryTree(root.right)) + 1
