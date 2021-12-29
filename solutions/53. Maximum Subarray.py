class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
#         Time Limit Exceeded
        # if len(nums)==1: return nums[0]        
        # maxSum = nums[0]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         a = sum(nums[i:j])
        #         if maxSum < a:
        #             maxSum = a
        # return maxSum
        
#         O(n) Time Complexity Solution
        if len(nums)==1: return nums[0]
        maxSum = nums[0]
        runningSum = 0
        for num in nums:
            if runningSum < 0:
                runningSum = num
            else:
                runningSum += num
            if runningSum > maxSum:
                maxSum = runningSum
        return maxSum
        
