class Solution(object):
    def customSortString(self, order, s):
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        res = []
        for c in order:
            i = ord(c) - ord('a')
            res.append (c* count[i])
            count[i] = 0
        
        for i in range(26):
            if count[i]:
                res.append(chr(i + ord('a')) * count[i])
        return "".join(res)