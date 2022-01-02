class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            cur = []
            for i in res:
                cur.append(i+[num])
            res += cur
        return res
        
