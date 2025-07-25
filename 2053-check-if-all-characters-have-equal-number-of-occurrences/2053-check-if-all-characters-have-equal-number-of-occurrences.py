from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count=defaultdict(int)
        for ch in s:
            count[ch]+=1
        
        res=count.values()
        return len(set(res))==1