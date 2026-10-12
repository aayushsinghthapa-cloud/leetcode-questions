class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        n = len(nums)
        half = (n + 1) // 2

        res = [0] * n
        res[::2] = nums[:half]
        res[1::2] = nums[half:]

        return res