class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            time = (target-position[i])/speed[i]
            arr.append((position[i],time))
        arr.sort(reverse = True)
        fleets = 0
        slowestTime =0
        for p,t in arr:
            if t>slowestTime:
                fleets+=1
                slowestTime =t
        return fleets