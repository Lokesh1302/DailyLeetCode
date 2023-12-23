class Solution:
    def isPathCrossing(self, path: str) -> bool:
        d = {'N' : [0, 1], 'E': [1, 0], 'S': [0, -1], 'W': [-1, 0]}
        startX = 0
        startY = 0
        visited = {(0,0)}
        for i in path:
            c = d[i]
            startX += c[0]
            startY += c[1]
            if (startX, startY) in visited:
                return True
            visited.add((startX, startY))
        return False
