class Solution:
    def reverseWords(self, s: str) -> str:
        i=0
        l=s.split()
        j=len(l)
        while i<j:
            l[i]=l[i][::-1]
            i+=1
        return " ".join(l)
        