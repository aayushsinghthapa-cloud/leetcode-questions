class Solution(object):
    def numRescueBoats(self, people, limit):
        boats = 0
        left, right = 0, len(people) - 1

        people.sort()

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            
            right -= 1
            boats += 1
        
        return boats