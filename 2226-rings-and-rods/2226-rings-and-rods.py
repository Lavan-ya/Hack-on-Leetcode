from collections import defaultdict
class Solution:
    def countPoints(self, rings: str) -> int:
        count=0
        sets=defaultdict(set)
        for i in range(0,len(rings),2):
            sets[rings[i+1]].add(rings[i])
        
        for key,value in sets.items():
            if len(value)==3:
                count+=1
        return count