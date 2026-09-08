class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)

        row_map = {}
        for row in grid:
            key = tuple(row)
            row_map[key] = row_map.get(key, 0) + 1

        count = 0

        for col in range(n):
            column = []
            for row in range(n):
                column.append(grid[row][col])

            column_key = tuple(column)

            if column_key in row_map:
                count += row_map[column_key]

        return count