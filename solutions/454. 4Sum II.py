class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
#         Time Limit Exceeded
        # res = 0
        # h1 = {}
        # for i in range(len(nums1)):
        #     h1[i] = nums1[i]
        # h2 = {}
        # for j in range(len(nums2)):
        #     for i in h1.keys():
        #         h2[(i,j)] = h1[i] + nums2[j]
        # h3 = {}
        # for j in range(len(nums3)):
        #     for i in h2.keys():
        #         h3[(*i,j)] = h2[i] + nums3[j]
        # h4 ={}
        # for j in range(len(nums3)):
        #     for i in h3.keys():
        #         h4[(*i,j)] = h3[i] + nums4[j]
        #         if h4[(*i,j)] == 0:
        #             res += 1
        # return res
        
#         Use pairing 
        p1 = collections.Counter(a+b for a in nums1 for b in nums2)
        return sum(p1[-c-d] for c in nums3 for d in nums4)
