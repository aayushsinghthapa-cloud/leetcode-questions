class Solution(object):
    def countCommas(self, n):
        commas = 0
        length = 1
        start = 1

        while start <= n:
            end = min(n, start * 10 - 1)

            count_numbers = end - start + 1
            commas_per_number = (length - 1) // 3

            commas += count_numbers * commas_per_number

            start *= 10
            length += 1

        return commas