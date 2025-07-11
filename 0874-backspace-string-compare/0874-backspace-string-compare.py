class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def remove(s):
            stack=[]
            for letter in s:
                if letter=='#' and stack:
                    stack.pop()
                elif letter!="#":
                    stack.append(letter)
            return stack

        return remove(s)==remove(t)