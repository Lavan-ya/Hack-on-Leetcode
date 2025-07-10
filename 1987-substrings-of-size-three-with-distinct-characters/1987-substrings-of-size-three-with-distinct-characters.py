class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        for r in range(len(s)-2):
            l=r
            seen=set()
            while l<r+3:
                if s[l] not in seen:
                    seen.add(s[l])
                    l+=1
                else:
                    break
            if len(seen)==3:
                count+=1
        return count