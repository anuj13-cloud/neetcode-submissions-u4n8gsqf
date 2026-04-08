class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for c in strs:
            string += str(len(c))+"#"+c
        return string 
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            i=j+1
            j=length+i
            result.append(s[i:j])
            i=j
        return result

       


