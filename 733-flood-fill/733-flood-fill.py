class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        stack = [(sr, sc)]
        color = image[sr][sc]
        d = [(1,0), (0,1), (-1,0), (0,-1)]
        vis = set()
        while stack:
            i, j = stack.pop()
            vis.add((i,j))
            image[i][j] = newColor
            for dx,dy in d:
                x, y = i+dx, j+dy
                if 0<=x<m and 0<=y<n and image[x][y]==color and (x,y) not in vis:
                    stack.append((x,y))
        return image