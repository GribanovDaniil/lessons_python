class Solution(object):
    def maxProfit(self, prices):
        cur_max = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                cur_max += prices[i] - prices[i - 1]

        return cur_max
#сложность O(n)
#находим максимальную выгоду с покупок одной акции