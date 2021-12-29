class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        for i in range(nums[0]):
            if self.canJump(nums[i+1:]):
                return True
        return False
        
        
        
        
        
