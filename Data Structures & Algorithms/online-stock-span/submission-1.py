class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        current_span=1

        if not self.stack:
            self.stack.append((price, 1))
            return current_span
        
        while self.stack:
            if price >= self.stack[-1][0]:
                current_span+=self.stack[-1][1]
                self.stack.pop()
            else:
                break
        self.stack.append((price, current_span))
        return current_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)