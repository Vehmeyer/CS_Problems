"""
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Implement a queue using two stacks.

You are given an array of requests, where requests[i] can be "push <x>" or "pop". Return an array composed of the results of each "pop" 
operation that is performed.
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        left.push(x)

    def remove():
        while not left.isEmpty():
            element = left.pop()
            right.push(element)
        returnElement = right.pop()
        
        while not right.isEmpty():
            element = right.pop()
            left.push(element)
        
        return returnElement
                    
    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans

"""
Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. 
Your task is to determine whether or not the sequence is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

An empty bracket sequence is a valid bracket sequence.
If S is a valid bracket sequence then (S), [S] and {S} are also valid.
If A and B are valid bracket sequences then AB is also valid.
"""

def validBracketSequence(sequence):
    openingBrackets = "([{"
    closingBrackets = ")]}"
    matchingBrackets = {")": "(", "]": "[", "}": "{"}
    stack = []
    
    for bracket in sequence:
        if bracket in openingBrackets:
            stack.append(bracket)
        elif bracket in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBrackets[bracket]:
                stack.pop()
            else:
                return False
    return len(stack) == 0