class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        left = 0
        right = 1
        while len(prices)>right:
            if prices[left] >= prices[right]:
                left = right
                right += 1
            elif prices[right] > prices[left]:
                profit = max(profit, prices[right] - prices[left])
                right += 1
        return profit

a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))