class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        for x in range(len(words)):
            word=words[x]
            n=len(word)
            if word==s[:n]:
                count+=1
        return count