class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen ={}
        for i in range(n):
            seen[nums[i]] = i
        
        for j in range(n):
            complement = target - nums[j]
            if complement in seen and j!=seen[complement]:
                return [j, seen[complement]]
        
        return []