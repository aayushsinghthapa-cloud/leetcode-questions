class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater_map = {}

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater_map[stack.pop()] = num
            stack.append(num)

        return [next_greater_map.get(num, -1) for num in nums1]