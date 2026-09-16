class Solution(object):
    def isPerfectSquare(self, num):
        if num == 1:
            return True

        left, right = 0, num // 2

        while(left <= right):
            mid = (left + right) // 2
            meow = mid * mid

            if(meow == num):
                return True
            elif(meow < num):
                left = mid + 1
            else:
                right = mid - 1
        return False