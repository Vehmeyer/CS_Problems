#Given two strings a and b, determine if they are isomorphic.
#Two strings are isomorphic if the characters in a can be replaced to get b.
#All occurrences of a character must be replaced with another character while preserving the order of characters. 
#No two characters may map to the same character but a character may map to itself.

def csIsomorphicStrings(a, b):
    if len(a) != len(b):
        return False
    if a == "" and b == "":
        return True
        
    a_map = {}
    b_map = {}
    
    for i in range(0, len(a)):
        a_char = a[i]
        b_char = b[i]
        
        if a_char not in a_map:
            a_map[a_char] = b_char
        if b_char not in b_map:
            b_map[b_char] = a_char
        if b_map[b_char] != a_char or a_map[a_char] != b_char:
            return False
    return True

#Given a pattern and a string a, find if a follows the same pattern.
#Here, to "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in a.

def csWordPattern(pattern, a):
    result = {}
    words = a.split(" ")
        
    if len(pattern) != len(words):
        return False
        
    for i in range(len(words)):
        curr_char = pattern[i]
        curr_word = words[i]
        
        if curr_char in result:
            if curr_word != result[curr_char]:
                return False
        else:
            if curr_word in result.values():
                return False
            result[curr_char] = curr_word
    
    return True

#Given an array of strings strs, write a function that can group the anagrams. The groups should be ordered such that the larger groups come first, 
#with subsequent groups ordered in descending order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
#typically using all the original letters exactly once.

def csGroupAnagrams(strs):
    results = {}
    
    for words in strs:
        sorted_word = "".join(sorted(words))
        if sorted_word in results:
            results[sorted_word].append(words)
        else:
            results[sorted_word] = [words]
    
    return list(results.values())