class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        points=[0]
        ans=0
        for i in range(len(gain)):
            points.append(points[-1]+gain[i])
            ans=max(ans,points[-1])
        return ans