class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0
        incre=1
        i=0
        while i<=n:
            sums=i+incre
            i=sums
            count+=1
            incre+=1
        return count-1
