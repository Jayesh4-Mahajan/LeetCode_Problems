class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         Solution 1
        # if len(nums) == 1:
        #     return nums[0]
        # nums.sort()
        # i = 0
        # while i < len(nums) - 1:
        #     if nums[i] != nums[i+1]:
        #         return nums[i]
        #     i += 2
        # return nums[-1]
        
#         Solution 2
        # if len(nums) == 1: return nums[0]
        # return 2*sum(set(nums)) - sum(nums)
        
#         Solution 3
        a = collections.Counter(nums)
        for key in a:
            if a[key] == 1:
                return key
        
