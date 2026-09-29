class Solution(object):
    def maxProfit(self, prices):
        left, right = 0, 1
        profit = 0

        while(right < len(prices)):
            if prices[left] < prices[right]:
                profit = profit + (prices[right] - prices[left])
            right += 1
            left += 1
        return profit