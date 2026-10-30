class Solution(object):
    def maxAscendingSum(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            
            max_sum = max(max_sum, current_sum)
        return max_sum
