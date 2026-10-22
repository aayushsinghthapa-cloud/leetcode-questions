class StockSpanner(object):

    def __init__(self):
        self.stack = []        # pairs (price, span), prices strictly decreasing from bottom to top

    def next(self, price):
        span = 1               # today always counts itself
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]       # absorb a whole earlier run in one step
        self.stack.append((price, span))
        return span