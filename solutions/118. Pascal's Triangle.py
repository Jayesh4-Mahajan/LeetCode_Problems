class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(2,numRows+1):
            prev = res[-1]
            curr = []
            for j in range(i):
                if j == 0 or j == i-1:
                    curr.append(1)
                else:
                    curr.append(prev[j-1]+prev[j])
            res.append(curr)
        return res
