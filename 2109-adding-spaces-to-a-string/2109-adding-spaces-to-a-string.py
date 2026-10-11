class Solution(object):
    def addSpaces(self, s, spaces):
        res = []
        j = 0                                         # next space index we're waiting for

        for i, c in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                res.append(" ")
                j += 1
            res.append(c)
        return "".join(res)