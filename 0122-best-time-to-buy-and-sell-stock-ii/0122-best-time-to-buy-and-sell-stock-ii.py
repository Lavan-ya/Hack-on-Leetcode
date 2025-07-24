class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0
        for sell in prices[1:]:
            if sell>buy:
                profit=profit+sell-buy
            buy=sell
        return profit