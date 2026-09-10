class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        lenPrices=len(prices)

        for i in range(lenPrices-1):
            for j in range(i+1,lenPrices):
                if((prices[j]-prices[i])>maxProfit):
                    maxProfit=prices[j]-prices[i]

        return maxProfit