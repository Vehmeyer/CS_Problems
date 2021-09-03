#Given a string (the input will be in the form of an array of characters), write a function that returns the reverse of the given string.
def csReverseString(chars):
    start = 0
    end = len(chars) - 1
    
    while start < end:
        storage = chars[start]
        chars[start] = chars[end]
        chars[end] = storage
        start += 1
        end -= 1
    return chars

#A palindrome is a word, phrase, number, or another sequence of characters that reads the same backward or forward. 
#This includes capital letters, punctuation, and other special characters.
#Given a string, write a function that checks if the input is a valid palindrome.

def csCheckPalindrome(input_str):
    start = input_str[0]
    end = input_str[len(input_str) - 1]
    
    for i in range(len(input_str)):
        if start == end:
            return True
        else: 
            return False

#Given a string, write a function that removes all duplicate words from the input. 
#The string that you return should only contain the first occurrence of each word in the string.

def csRemoveDuplicateWords(input_str):
    stringDictionary = {}
    resultsDictionary = {}
    splitString = input_str.split()
    results = ""

    for key, value in enumerate(splitString):
        stringDictionary[key] = value
        
    for key, value in stringDictionary.items():
        if value not in resultsDictionary.values():
            resultsDictionary[key] = value
    
    results = " ".join(str(value) for value in resultsDictionary.values())
    
    return results
