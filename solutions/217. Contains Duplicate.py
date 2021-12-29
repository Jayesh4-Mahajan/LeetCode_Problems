class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         One Line Solution
        # return not len(set(nums)) == len(nums)
        
        if len(nums) <= 1:
            return False
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False
