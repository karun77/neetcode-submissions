from collections import deque

class Solution:

    def bfs(self,row,col,visit,rowLen,colLen,grid):
        #pseudcode treating this like a graph
        queue = deque()
        queue.append((row,col))

        while(queue):
            (row,col) = queue.popleft()
            visit.add((row,col))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for n in directions:
                dr = n[0]
                dc = n[1]
                if  (row+dr) in range(len(grid)) and (col+dc) in range(len(grid[0])) and (row+dr,col+dc) not in visit and grid[row+dr][col+dc]=="1":
                        queue.append((row+dr,col+dc))
                        visit.add((row+dr,col+dc))

        return 

    def numIslands(self, grid: List[List[str]]) -> int:

        visit = set()
        count = 0

        rowLen = len(grid)
        colLen = len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="1" and (row,col) not in visit:
                    count+=1
                    self.bfs(row,col,visit,rowLen,colLen,grid)

        return count
        



        