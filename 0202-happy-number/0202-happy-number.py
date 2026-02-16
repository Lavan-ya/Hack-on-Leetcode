class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        sums=0
        while n!=1:
            if len(str(n))>1:
                while(n!=0):
                    r=n%10
                    sums+=r*r
                    n=n//10
            else:
                sums=n*n
            n=sums
            if sums not in s:
                s.add(sums)
                sums=0
            else:
                return False
        return True
