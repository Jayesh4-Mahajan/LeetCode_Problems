class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = collections.defaultdict(int)
        l = len(nums)
        for num in nums:
            h[num] += 1
            if h[num] >= l/2:
                return num
