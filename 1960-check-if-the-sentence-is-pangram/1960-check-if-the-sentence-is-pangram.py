class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sets = set()
        for i in range(len(sentence)):
            if sentence[i] not in sets:
                sets.add(sentence[i])
        if len(sets)==26:
            return True
        return False