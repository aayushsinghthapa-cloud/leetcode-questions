class Solution(object):
    def findAnagrams(self, s, p):
        k = len(p)
        if k > len(s):
            return []
        
        need = [0] * 26
        window = [0] * 26

        for c in p:
            need[ord(c) - ord('a')] += 1
        
        res = []
        for i, c in enumerate(s):
            window[ord(c) - ord('a')] += 1
            if i >= k:
                window[ord(s[i - k]) - ord('a')] -= 1
            if window == need:
                res.append(i - k + 1)
        return res