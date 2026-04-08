import heapq as hq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq.heapify(nums)
        n = len(nums)
        while n>k:
            hq.heappop(nums)
            n-=1
        
        res = hq.heappop(nums)
        return res

        