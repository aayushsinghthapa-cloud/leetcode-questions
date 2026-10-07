class Solution(object):
    def appendCharacters(self, s, t):
        j = 0
        for c in s:
            if j < len(t) and c == t[j]:
                j += 1
        return len(t) - j