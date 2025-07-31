from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        w=defaultdict(int)
        l=defaultdict(int)
        for i in range(len(matches)):
            for j in range(2):
                if j==0:
                    w[matches[i][j]]+=1
                else:
                    l[matches[i][j]]+=1
        
        aw=[]
        al=[]
        for x,y in w.items():
            if x not in l:
                aw.append(x)
        for x,y in l.items():
            if y==1:
                al.append(x)
        return [sorted(aw),sorted(al)]