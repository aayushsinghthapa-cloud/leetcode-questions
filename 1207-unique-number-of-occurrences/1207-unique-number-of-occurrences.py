class Solution(object):
    def uniqueOccurrences(self, arr):
        freq = {}

        # count frequency
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        seen = set()

        # check uniqueness of frequencies
        for count in freq.values():
            if count in seen:
                return False
            seen.add(count)

        return True