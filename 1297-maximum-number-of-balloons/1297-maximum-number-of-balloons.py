from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        words=set('balloon')
        dic=defaultdict(int)
        count=0

        for i in text:
            if i in words:
                dic[i]+=1
        
        while len(dic)==5:
            string='balloon'
            c=0
            for x in string:
                if x in dic:
                    dic[x]-=1
                    c+=1
                if dic[x]==0:
                    del dic[x]
            if c==7:
                count+=1
        
        return count
                   