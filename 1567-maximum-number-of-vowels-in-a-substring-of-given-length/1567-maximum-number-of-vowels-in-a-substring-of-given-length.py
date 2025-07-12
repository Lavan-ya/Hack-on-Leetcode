class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set('aeiou')
        count=0
        ans=0
        for r in range(k):
            if s[r] in vowels:
                count+=1
        ans=count

        for l in range(k,len(s)):
            if s[l] in vowels:
                count+=1
            if s[l-k] in vowels:
                count-=1
            ans=max(ans,count)
        return ans