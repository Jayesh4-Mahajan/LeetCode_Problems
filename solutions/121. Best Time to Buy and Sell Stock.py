class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for price in prices[1:]:
            a =  price - buy
            if a > 0:
                if a > profit:
                    profit = a
            else:
                buy = price
        
        return profit
