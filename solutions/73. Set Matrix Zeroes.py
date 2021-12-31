class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        columns = set()
        for i in range(m):
            row = matrix[i]
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
​
        for row in rows:
            for j in range(n):
                matrix[row][j] = 0
        for col in columns:
            for i in range(m):
                matrix[i][col] = 0
        
