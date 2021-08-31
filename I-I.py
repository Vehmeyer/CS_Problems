#Create a function that returns True if the given string has any of the following: Only letters and no numbers.
    #Only numbers and no letters.
#If a string has both numbers and letters or contains characters that don't fit into any category, return False.

def csAlphanumericRestriction(input_str):
    return input_str.isalpha() or input_str.isnumeric()

#Write a function that takes a string as input and returns that string in reverse order, 
#with the opposite casing for each character within the string.

def csOppositeReverse(txt):
    swappedCase = txt.swapcase()
    return swappedCase[::-1]

#Create a function that given an integer, returns an integer where every digit in the input integer is squared.

def csSquareAllDigits(n):
    squaredN = ''.join(str(int(i)**2) for i in str(n)) 
    return int(squaredN)

#Given a string, return a new string with all the vowels removed.

def csRemoveTheVowels(input_str): 
    result = ""
    for c in input_str:
        if c.lower() not in "aeiou":
            result += c 
    return result   
