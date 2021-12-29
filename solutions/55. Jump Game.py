class Solution:
    def canJump(self, nums: List[int]) -> bool:
#         Time Limit Exceeded
        # if len(nums) == 1:
        #     return True
        # if nums[0] == 0:
        #     return False
        # for i in range(nums[0]):
        #     if self.canJump(nums[i+1:]):
        #         return True
        # return False
        
#         Using Greedy : Going in reverse
        end = len(nums) - 1
        for i in range(end, -1, -1): # Using end instead of len(nums) reduces one more calculation which improves the runtime
            if i + nums[i] >= end:
                end = i
        return True if end == 0 else False
        
        
        
        
