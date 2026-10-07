class Solution(object):
    def lengthOfLastWord(self, s):
        text = s.rstrip()
        for k in range(len(text) - 1, -1, -1):
            if text[k] == " ":
                return len(text) - 1 - k   # characters after the space
        return len(text)   