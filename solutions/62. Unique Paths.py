class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        visited = {(1,1): 1, (2,1): 1, (1,2): 1}
​
        def paths(m, n):
            if (m,n) in visited: 
                return visited[(m,n)]
            elif m -1 > 0 and n -1 > 0:
                visited[(m-1,n)] = paths(m-1,n)
                visited[(m, n-1)] = paths(m,n-1)
                return visited[(m-1,n)] + visited[(m, n-1)]
            elif m - 1 > 0:
                visited[(m-1,n)] = paths(m-1,n)
                return visited[(m-1,n)]
            else:
                visited[(m, n-1)] = paths(m,n-1)
                return visited[(m, n-1)]         
        
        visited[(m, n)] = paths(m, n)
        return visited[(m, n)]
