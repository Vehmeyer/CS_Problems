#Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. 
#If Bob is not in the array, return -1

def csWhereIsBob(names):
    for name in names:
        if name == "Bob":
            return names.index("Bob")
    return -1

#Imagine a school that children attend for years. In each year, there are a certain number of groups started, marked with the letters. 
#So if years = 7 and groups = 4For the first year, the groups are 1a, 1b, 1c, 1d, and for the last year, the groups are 7a, 7b, 7c, 7d.
#Write a function that returns the groups in the school by year (as a string), separated with a comma and space in the form of 
# "1a, 1b, 1c, 1d, 2a, 2b (....) 6d, 7a, 7b, 7c, 7d".

def csSchoolYearsAndGroups(years, groups):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final = []
    
    for year in range(1, years + 1):
        for letter in alphabet[:groups]:
            final.append(str(year) + letter)
    return ", ".join(final)

#Create a function that concatenates the number 7 to the end of every chord in a list. If a chord already ends with a 7, do not add another 7.

def csMakeItJazzy(chords):
    final = []
    for chord in chords:
        if chords == []:
            return []
        elif "7" in chord:
            final.append(f"{chord}")
        else:
            final.append(f"{chord}7")
    return final

#Given a string of words, return the length of the shortest word(s).

def csShortestWord(input_str):
    splitString = input_str.split()
    sortedString = sorted(splitString, key=len)
    return len(sortedString[0])

#Given an array of integers, return the sum of all the positive integers in the array.

def csSumOfPositive(input_arr):
    positiveNums = []
    for num in input_arr:
        if num > 0:
            positiveNums.append(num)
    return sum(positiveNums)

#Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the 
#range (except integers that contain the digit 5).

def csAnythingButFive(start, end):
    numbers = []
    for num in range(start, end):
        strNum = str(num)
        if "5" in strNum:
            continue
        else:
            numbers.append(strNum)
    return len(numbers) + 1
