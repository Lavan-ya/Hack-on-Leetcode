class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        l,r=0,1
        ans=0
        if len(s)<2:
            return 1
        while r<len(s):
            if ord(s[r]) != ord(s[r-1]) + 1:
                l=r
                r+=1
            elif ord(s[r]) == ord(s[r-1]) + 1:
                r+=1
            ans=max(ans,r-l)
        return ans