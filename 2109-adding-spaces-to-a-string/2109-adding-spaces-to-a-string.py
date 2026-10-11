class Solution(object):
    def addSpaces(self, s, spaces):
        spaces = spaces[::-1]
        res = []

        for i in range(len(s)):
            if spaces and i == spaces[-1]:   # is a space due before this character?
                res.append(" ")
                spaces.pop()                 # done with this index, expose the next one
            res.append(s[i])                 # the character is always added
        return "".join(res)