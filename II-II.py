#You are given a non-empty array of integers.
#One element appears exactly once, with every other element appearing at least twice, perhaps more.
#Write a function that can find and return the element that appears exactly once.

def csFindTheSingleNumber(nums):
    num_dict = {}
    result = []
    
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 0
        num_dict[num] += 1
    for key, value in num_dict.items():
        if value == 1:
            result.append(key)
    
    return result[0]

#Given a list of different students' scores, write a function that returns the average of each student's top five scores. 
#You should return the averages in ascending order of the students' id numbers.
#Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). 
#The averages should be calculated using integer division.

def csAverageOfTopFive(scores):
    scores.sort(reverse = True)
    print(scores)
    
    result = []
    current = []
    index = scores[0][0]
    
    for key, value in scores:
        if key == index:
            if len(current) < 5:
                current.append(value)
        else:
            result.append([index, sum(current) // len(current)])
            current = [value]
            index = key
    result.append([index, sum(current) // len(current)])
    result = result[::-1]
    return result

#Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.
#You can use each character in text at most once.
#Write a function that returns the maximum number of instances of "lambda" that can be formed.

def csMaxNumberOfLambdas(text):
    letters = {}
    result = []
    
    for letter in text:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1
    
    for key, value in letters.items():
        if key == "l" or key == "a" or key == "m" or key == "b" or key == "d" and value >= 1:
            result.append(value)
        elif key == "l" or key == "a" or key == "m" or key == "b" or key == "d" not in letters:
            return 0
        
    return min(result)