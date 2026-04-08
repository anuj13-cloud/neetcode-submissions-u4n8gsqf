class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        substring = []

        def backtrack(openN,closeN):
            if openN == closeN == n:
                res.append("".join(substring))
                return
            if openN <n:
                substring.append("(")
                backtrack(openN+1,closeN)
                substring.pop()
            if closeN < openN:
                substring.append(")")
                backtrack(openN,closeN+1)
                substring.pop()

            
        backtrack(0,0)
        return res

