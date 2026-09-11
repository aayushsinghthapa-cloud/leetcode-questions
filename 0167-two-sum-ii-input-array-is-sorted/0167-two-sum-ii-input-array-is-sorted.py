class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while (left < right):
            total = numbers[right] + numbers[left]

            if total == target:
                return ([left + 1, right + 1])
            
            elif total < target:
                left += 1
            
            else:
                right -= 1
            