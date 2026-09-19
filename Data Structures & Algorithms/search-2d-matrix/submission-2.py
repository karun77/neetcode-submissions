class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #check if target lies within bounds
        if (target<matrix[0][0]) or (target>matrix[-1][-1]):
            return False

        #which row is the target in
        start_row = 0
        end_row = len(matrix)-1
        middle_row = int((start_row+end_row)/2)

        while start_row < end_row:
            if (target>=matrix[middle_row][0]) and (target<=matrix[middle_row][-1]):
                break
            elif target > matrix[middle_row][-1]:
                start_row = middle_row+1
            else:
                end_row = middle_row-1
            middle_row = int((start_row+end_row)/2)

        start_col = 0
        end_col = len(matrix[0])-1
        middle_col = int((start_col+end_col)/2)

        while start_col!=end_col:
            if (end_col)==(start_col+1): # edge case for when only two elements in the search space
                if target==matrix[middle_row][middle_col]:
                    return True                
                elif target==matrix[middle_row][middle_col+1]:
                    return True
                else:
                    return False
            if target==matrix[middle_row][middle_col]:
                return True
            elif target>matrix[middle_row][middle_col]:
                start_col=middle_col+1
            else:
                end_col=middle_col-1
            middle_col=int((start_col+end_col)/2)

        if target==matrix[middle_row][middle_col]:
            return True
        
        return False
