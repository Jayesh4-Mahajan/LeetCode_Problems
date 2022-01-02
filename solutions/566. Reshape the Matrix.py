class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        a = []
        if m*n != r*c:
            return mat
        res = []
        cur = []
        for i in range(m*n):
            if len(cur) < c:
                cur.append(mat[i//n][i%n])
            else:
                res.append(cur)
                cur = [mat[i//n][i%n]]
        if len(cur) > 0:
            res.append(cur)
        return res
