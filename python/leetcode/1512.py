# https://leetcode.com/problems/number-of-good-pairs/

def numIdenticalPairs(nums):
    num = 0
    for i in range(len(nums)):       
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and i < j:
                num += 1
    return num


    
    
print(numIdenticalPairs([1,2,3,1,1,3]))