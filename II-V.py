#Two words are blanagrams if they are anagrams but exactly one letter has been substituted for another.
#Given two words, check if they are blanagrams of each other.

def checkBlanagrams(word1, word2):
    difference = 0
    
    sortedWord1 = sorted(word1)
    sortedWord2 = sorted(word2)

    for a, b in zip(sortedWord1, sortedWord2):
        if sortedWord1 == sortedWord2:
            return False
        if a != b:
            difference += 1
        if difference > 1:
            return False
        return True

#You are given a sorted array in ascending order that is rotated at some unknown pivot (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]) 
#and a target value.
#Write a function that returns the target value's index. If the target value is not present in the array, return -1.
#You may assume no duplicate exists in the array.
#Your algorithm's runtime complexity must be in the order of O(log n).

def findValueSortedShiftedArray(nums, target):
    min = 0
    max = len(nums) - 1
    
    while min < max:
        mid = (min + max) // 2
        
        if nums[mid] == target:
            return mid
            
        if nums[min] <= nums[mid]:
            if target >= nums[min] and target < nums[mid]:
                max = mid
            else:
                min = mid + 1
            
        else:
            if target <= nums[max] and target > nums[mid]:
                min = mid + 1
            else:
                max = mid
    return -1