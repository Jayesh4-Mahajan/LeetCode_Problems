class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # s = set(nums1)
        # res = []
        # for num in nums2:
        #     if num in s:
        #         res.append(num)
        #         s.remove(num)
        # return res
        s1 = set(nums1)
        s2 = set(nums2)
        return list(s1.intersection(s2))
