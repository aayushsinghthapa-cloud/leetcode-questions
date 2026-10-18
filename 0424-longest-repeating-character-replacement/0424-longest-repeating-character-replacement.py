class Solution(object):
    def characterReplacement(self, s, k):
        count = [0] * 26                 # count[0] for 'A', ..., count[25] for 'Z'
        left = 0
        max_freq = 0                     # highest single-letter count seen in any window so far
        best = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            max_freq = max(max_freq, count[idx])

            if (right - left + 1) - max_freq > k:    # too many replacements needed
                count[ord(s[left]) - ord('A')] -= 1  # drop the leftmost letter
                left += 1

            best = max(best, right - left + 1)
        return best