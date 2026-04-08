class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        j = 1
        maxint = j
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                j+=1
            elif nums[i] > nums[i-1] +1:
                j = 1
            if j>maxint:
                maxint = j
        return maxint
            
        
