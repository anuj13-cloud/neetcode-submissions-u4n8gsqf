import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for nums in stones:
            hq.heappush(maxheap, -nums)
        while len(maxheap)>1:
            stone1 =hq.heappop(maxheap)
            stone2 = hq.heappop(maxheap)
            if abs(stone1)>abs(stone2):
                newstone = abs(stone1)-abs(stone2)
            else:
                newstone = abs(stone2)-abs(stone1)
            hq.heappush(maxheap,-newstone)
        return -maxheap[0]
                  

        