class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l =sentence.split()
        total=len(searchWord)
        for i in range(len(l)):
            print(l[i][0:total])
            print(searchWord)
            if l[i][0:total]==searchWord:
                return i+1
        return -1
        