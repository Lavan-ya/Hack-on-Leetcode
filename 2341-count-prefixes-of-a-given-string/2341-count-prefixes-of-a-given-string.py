class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        for x in range(len(words)):
            l,r=0,0
            word=words[x]
            if len(word) > len(s):
                continue
            while l<len(word) and r < len(s):
                if word[l]!=s[r]:
                    break
                else:
                    l+=1
                    r+=1 
            if l==len(word):
                count+=1
        return count