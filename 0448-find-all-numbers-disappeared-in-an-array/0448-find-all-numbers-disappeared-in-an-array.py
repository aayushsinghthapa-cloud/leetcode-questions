class Solution(object):
    def findDisappearedNumbers(self, nums):
        num = set(nums)

        max_num = len(nums)

        answer = []
        i = 1
        while (i <= max_num):
            if i not in num:
                answer.append(i)
            i +=1
        
        return answer