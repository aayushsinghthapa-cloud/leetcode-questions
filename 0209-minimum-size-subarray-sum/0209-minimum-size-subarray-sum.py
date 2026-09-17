class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = total = 0
        result = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while (total >= target):
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if result == float('inf') else result