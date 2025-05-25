# Monotonic Stack:
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []

        i = n - 1
        while i >= 0:
            while len(stack) and stack[-1] > prices[i]:
                stack.pop()
            temp = prices[i]
            if len(stack):
                prices[i] -= stack[-1]
            stack.append(temp)
            i -= 1

        return prices
