class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l=list(s)
        for i in range(0,len(s),2*k):
            start=i
            end = min(i+(k-1),len(s)-1)
            while start<end:
                l[start],l[end]=l[end],l[start]
                start+=1
                end-=1
        return "".join(l)
            