class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        target = len(nums) // 2
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > target:
                return num