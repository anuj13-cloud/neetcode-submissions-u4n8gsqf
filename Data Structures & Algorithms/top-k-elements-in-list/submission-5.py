class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            count[num] = 1 +count.get(num,0)
        for num,cnt in count.items():
            freq[cnt].append(num)
        res=[]
        for i in range(len(freq)-1,-1,-1):
            for i in freq[i]:
                res.append(i)
            if len(res) ==k:
                return res

