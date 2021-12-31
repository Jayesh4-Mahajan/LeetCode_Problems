class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
        
        c = Counter(nums1)
        res = []
        for e in nums2:
            if e in c:
                if c[e] > 0:
                    res.append(e)
                    c[e] -=1
        return res
        
