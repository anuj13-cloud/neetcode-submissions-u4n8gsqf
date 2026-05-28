class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = r
        while l<=r:
            k=(l+r)//2
            totalHour = 0
            for p in piles:
                totalHour+=math.ceil(float(p)/k)
            if totalHour<=h:
                res = k
                r = k-1
            else:
                l=k+1
        return res