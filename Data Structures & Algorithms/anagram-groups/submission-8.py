class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list[str])
        for string in strs:
            sortedString = "".join(sorted(string))
            res[sortedString].append(string)
        
        return list(res.values())
            
