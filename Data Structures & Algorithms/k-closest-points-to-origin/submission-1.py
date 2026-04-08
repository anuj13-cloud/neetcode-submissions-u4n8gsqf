import heapq as hq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        res = []
        hashmap = {}
        for point in points:
            dist = math.sqrt(math.pow(point[0],2)+math.pow(point[1],2))
            hq.heappush(pq,(-dist,point))
        n = len(pq)
        while n>k:
            hq.heappop(pq)
            n-=1
        for item in pq:
            res.append(item[1])

        
        return res







        