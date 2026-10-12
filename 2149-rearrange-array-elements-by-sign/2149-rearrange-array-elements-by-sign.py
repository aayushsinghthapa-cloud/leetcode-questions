class Solution(object):
    def rearrangeArray(self, nums):
        pos, neg = [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        res = []
        for k in range(len(nums) // 2):
            res.append(pos[k])     # kth positive
            res.append(neg[k])     # paired with the kth negative
        return res