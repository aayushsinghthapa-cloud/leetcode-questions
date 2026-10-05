class Solution(object):
    def evalRPN(self, tokens):
        def div(a, b):
            q = abs(a) // abs(b)
            return q if (a < 0) == (b < 0) else -q

        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": div,
        }
        stack = []

        for t in tokens:
            if t in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[t](a, b))
            else:
                stack.append(int(t))

        return stack[-1]