class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()

        for num in range(len(nums) - 1):
            if nums[num] == nums[num + 1]:
                return nums[num]
            