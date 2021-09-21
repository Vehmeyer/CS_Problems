"""
Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. 
Your function should return a reference to the head of the updated linked list.

Example:
Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.
"""
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def condense_linked_list(node):
    if node is None:
        return None
    
    current = node
    while current is not None:
        new = current
        while new.next is not None:
            if new.next.value == current.value:
                new.next = new.next.next
            else:
                new = new.next
        current = current.next
    
    return node

"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. 
If there is no such character, return '_'.
"""

def first_not_repeating_character(s):
    count = {}
    char = list(s)
    for i in range(len(char)):
        if char[i] not in count:
            count[char[i]] = 1
        else:
            count[char[i]] += 1
    for key, value in count.items():
        if value == 1:
            for i in range(len(s)):
                if key == s[i]:
                    return key
           
    return "_"

"""
In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.

The spy, if it exists:

Does not trust anyone else.
Is trusted by everyone else (he's good at his job).
Works alone; there are no other spies in the city-state.
You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.

If the spy exists and can be found, return their identifier. Otherwise, return -1.
"""

def uncover_spy(n, trust):
    in_range = [0] * (n + 1)
    out_range = [0] * (n + 1)
    
    for a, b in trust:
        out_range[a] += 1
        in_range[b] += 1
        
    for i in range(1, n + 1):
        if in_range[i] == n - 1 and out_range[i] == 0:
            return i
            
    return -1
