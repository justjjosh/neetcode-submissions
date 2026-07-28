class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_profit = 0
        while j < len(prices):
            buy_price = prices[i]
            sell_price = prices[j]
            if buy_price < sell_price:
                profit = sell_price - buy_price
                max_profit = max(profit, max_profit)

            else:
                i = j

            j += 1
        return max_profit

        
        