class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_len = len(grid)
        col_len = len(grid[0])

        row_count = [0] * row_len
        col_count = [0] * col_len

        for i in range(row_len):
            for j in range(col_len):
                row_count[i] += grid[i][j]
                col_count[j] += grid[i][j]

        diff = [[0]*col_len for i in range(row_len)]
        for i in range(row_len):
            for j in range(col_len):
                diff[i][j] = 2 * (row_count[i] + col_count[j]) - row_len - col_len

        return diff
