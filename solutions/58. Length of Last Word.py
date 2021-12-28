class Solution:
    def lengthOfLastWord(self, s: str) -> int:
##         Solution 1:
        # res = [x for x in s.split(' ') if x != '']
        # return len(res[-1])
        
##          Solution 2:
        return len(s.split()[-1])
