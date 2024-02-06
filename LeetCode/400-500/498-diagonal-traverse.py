class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        d= collections.defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                d[i+j].append(matrix[i][j])
        ans= []
        for entry in d.items():
            if entry[0] % 2 == 0:
                ans.extend(entry[1][::-1])
            else:
                ans.extend(entry[1])
        return ans
