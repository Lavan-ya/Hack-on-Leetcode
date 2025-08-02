class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s)-1):
            value=s[i:i+2]
            reverse=value[::-1]
            if reverse in s:
                return True
        return False
        