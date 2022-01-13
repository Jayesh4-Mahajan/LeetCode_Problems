class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            c = nums[i]
            l = i+1
            r = len(nums)-1
            prev_b = ""
​
            while c <= 0 and l < r:
​
                if i>0 and c == nums[i-1]:
                    break
​
                b = nums[l]
                a = -(b+c)
​
                if nums[r] == a and prev_b != b:
                    res.append([nums[i], nums[l], nums[r]])
                    prev_b = b
                    l += 1
                elif nums[r] > a:
                    r -= 1
                else:
                    l +=1
                    
        return res
        
        
