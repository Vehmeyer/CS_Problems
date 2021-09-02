#You are given the prices of a stock, in the form of an array of integers, prices. Let's say that prices[i] is the price of the stock 
# on the ith day (0-based index). Assuming that you are allowed to buy and sell the stock only once, your task is to find the maximum 
# possible profit (the difference between the buy and sell prices).

def buyAndSellStock(prices):
    maxProfit = 0
    buyDay = 0
    for i in range(1, len(prices)):
        maxProfit = max(maxProfit, prices[i] - prices[buyDay])
        if prices[buyDay] > prices[i]:
            buyDay = i
    return maxProfit

#Given a string, your task is to replace each of its characters by the next one in the English alphabet; 
#i.e. replace a with b, replace b with c, etc (z would be replaced by a).

def alphabeticShift(inputString):
    newKey = 1 % 26
    new = []
    for letter in inputString:
        new.append(getNew(letter, newKey))
    return "".join(new)
         
def getNew(letter, newKey):
    newLetter = ord(letter) + newKey
    return chr(newLetter) if newLetter <= 122 else chr(96 + newLetter % 122)

#You are given a parentheses sequence, check if it's regular.
#For s = "()()(())", the output should be validParenthesesSequence(s) = true;
#For s = "()()())", the output should be validParenthesesSequence(s) = false.

def validParenthesesSequence(s):
    stack = []
    
    if len(s) % 2 != 0:
        return False   
    
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            else:
                if i ==")" and stack.pop() != "(":
                    return False
                else:
                    pass
    if len(stack) != 0:
        return False
    return True