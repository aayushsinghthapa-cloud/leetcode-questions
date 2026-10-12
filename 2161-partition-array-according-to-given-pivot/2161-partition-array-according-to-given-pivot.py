class Solution(object):
    def pivotArray(self, nums, pivot):
        n = len(nums)
        res = [pivot] * n            # pre-fill, so the middle is already correct
        lo, hi = 0, n - 1

        for i in range(n):
            if nums[i] < pivot:      # front-to-back keeps the smaller ones in order
                res[lo] = nums[i]
                lo += 1
            if nums[n - 1 - i] > pivot:   # back-to-front keeps the larger ones in order
                res[hi] = nums[n - 1 - i]
                hi -= 1
        return res