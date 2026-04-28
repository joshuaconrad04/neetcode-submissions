class StockSpanner:

    def __init__(self):
        self.span = []

    def next(self, price: int) -> int:
        stack = self.span.copy()

        res = 1

        while stack:
            if stack[-1]<=price:
                stack.pop()
                res+=1
            else: 
                break
        self.span.append(price)
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)