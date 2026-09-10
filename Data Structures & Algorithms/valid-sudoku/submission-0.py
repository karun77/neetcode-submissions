class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check each row
        n = len(board)
        
        groupNo=[]
        groupValue=[]
        latestIndex=-1

        for row in range(n):
            for i in range(n-1):
                if board[row][i]==".":
                    continue
                for j in range(i+1,n):
                    if((board[row][i]==board[row][j]) and board[row][j]!="."):
                        return False

        #check each column
        for column in range(n):
            for i in range(n-1):
                if board[i][column]==".":
                    continue
                for j in range(i+1,n):
                    if((board[i][column]==board[j][column]) and board[j][column]!="."):
                        return False

        #check each box
        startPos = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        boxPos = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

        for t in range(n):
            for i in range(n-1):
                #print(str(startPos[t][1]))
                #print(str(boxPos[i][1]))
                if board[startPos[t][0]+boxPos[i][0]][startPos[t][1] + boxPos[i][1]]==".":
                    continue
                for j in range(i+1,n):
                    if((board[startPos[t][0]+boxPos[i][0]][startPos[t][1] + boxPos[i][1]]==board[startPos[t][0]+boxPos[j][0]][startPos[t][1] + boxPos[j][1]]) and board[startPos[t][0]+boxPos[j][0]][startPos[t][1] + boxPos[j][1]]!="."):
                        return False

        return True
        




