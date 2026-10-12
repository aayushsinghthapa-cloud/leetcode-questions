class Solution(object):
    def pivotArray(self, nums, pivot):
        low = []
        high = []
        equal = []

        for x in nums:
            if x < pivot:
                low.append(x)
            elif x > pivot:
                high.append(x)
            else:
                equal.append(x)
        return low + equal + high
        