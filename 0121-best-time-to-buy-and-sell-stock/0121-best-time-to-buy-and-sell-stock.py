class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0
        for sell in range(1,len(prices)):
            if prices[sell]<buy:
                buy=prices[sell]
            profit=max(profit,prices[sell]-buy)
        return profit