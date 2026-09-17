# Solving using Floyd's Cycle Detection
# We are sure to get a duplicate value for the given constraint
class Solution(object):
    def findDuplicate(self, nums):
        slow = fast = nums[0]

        # We are making slow, and fast meet inside a cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # We are moving both slow, and fast at the same speed to meet at the cycle entry
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow