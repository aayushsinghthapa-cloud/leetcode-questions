class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        n = len(skill)
        total = 0
        target = skill[0] + skill[-1]

        for i in range(n // 2):
            a, b = skill[i], skill[n - i - 1 ]
            if a + b != target:
                return -1
            total += a* b 
        return total