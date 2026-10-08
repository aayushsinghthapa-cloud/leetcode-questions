class Solution(object):
    def longestCommonPrefix(self, strs):
        answer = ""

        for i in range(len(strs[0])):
            for word in strs:
                if i >= len(word) or word[i] != strs[0][i]:
                    return answer

            answer += strs[0][i]

        return answer