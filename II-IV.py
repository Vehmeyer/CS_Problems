#For a given positive integer n determine if it can be represented as a sum of two Fibonacci numbers (possibly equal).

def fibonacciSimpleSum2(n):
    pass
    fibNums = [0,1,1,2,3,5,8,13,21]
    
    for i in range(len(fibNums)):
        next_num = fibNums[-1] + fibNums[-2]
        fibNums.append(next_num)
        
    for i in range(len(fibNums)):
        for j in range(i + 1, len(fibNums)):
            if fibNums[i] + fibNums[j] == n:
                return True
    return False

#Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search for target in nums. 
#If target exists, then return its index, otherwise, return -1.

def csBinarySearch(nums, target):
    min = 0
    max = len(nums) - 1
    
    while min <= max:
        mid = (min + max) // 2
        guess = nums[mid]
        if guess == target:
            return mid
        elif guess > target:
            max = mid -1
        else:
            min = mid + 1
    return -1

#Given an integer array nums sorted in ascending order, and an integer target.
#Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [1,2,3,4,5,6,7] might become [4,5,6,7,1,2,3]).
#You should search for target in nums and if found return its index, otherwise return -1.

def csSearchRotatedSortedArray(nums, target):
    #O(n) - solution
    #for i in range(len(nums)): 
    #    if nums[i] == target:
    #        return i      
    #return -1
    
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[end]:
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        elif nums[mid] < nums[end]:
            if target > nums[mid] and target <= nums[end]:
                start = mid + 1
            else:
                end = mid -1
                
    if nums[end] == target:
        return end
    else:
        return -1
