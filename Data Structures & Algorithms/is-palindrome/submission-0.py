class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for c in s:
            if c.isalnum():
                string +=c
        return string.lower() == "".join(reversed(string.lower()))

