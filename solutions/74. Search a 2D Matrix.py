class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        for i in range(len(matrix)-1):
            if target >= matrix[i][0] and target < matrix[i+1][0]:
                row = i
                break
        if target >= matrix[-1][0]:
            row = len(matrix) - 1
        for k, v in enumerate(matrix[row]):
            if v == target:
                return True
            elif target < v:
                return False
        
        return False
