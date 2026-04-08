class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            mult =1
            for i in range(0, len(nums)):
                if  i == nums.index(num):
                    continue
                mult = mult* nums[i]
            
            res.append(mult)
        return res