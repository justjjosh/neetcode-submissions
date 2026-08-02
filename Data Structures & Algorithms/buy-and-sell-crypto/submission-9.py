class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #profit, being able so sell for higher
        #two pointer, one keep track of buy and the other for sale
        #return max value of profit made
        profit_made = 0

        i, j = 0, 1
        while j < len(prices):
            #check if we can buy for higher than we are currently on
            current_price = prices[i]
            sell_price = prices[j]
            #if the price we can buy for is greater than sell price
            if current_price > sell_price:
                i += 1
            else:
                profit = sell_price - current_price
                profit_made = max(profit_made, profit)
                j += 1

        return profit_made
        