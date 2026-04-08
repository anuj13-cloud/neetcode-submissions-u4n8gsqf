class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        res = []
        c = len(nums)
        for i in range(c):
            j =1 
            k = i-1
            while(k>i-c):
                j*=nums[k]
                k-=1
            res.append(j)
        
        return res
            