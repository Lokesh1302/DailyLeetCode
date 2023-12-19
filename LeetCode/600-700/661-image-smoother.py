class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])

        neighbors = [[-1, -1], [-1, 0], [-1, 1],
                     [+0, -1], [+0, 0], [+0, 1],
                     [+1, -1], [+1, 0], [+1, 1]]
        
        result = [[0]*cols for i in range(rows)]

        for r in range(rows):
            for c in range(cols):
                count = 0
                sum = 0
                for i in neighbors:
                    new_r = r + i[0]
                    new_c = c + i[1]
                    if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols:
                        continue
                    count += 1
                    sum += img[new_r][new_c]
                result[r][c] = math.floor(sum/count)
        return result
