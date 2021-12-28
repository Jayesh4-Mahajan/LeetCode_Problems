class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = [x for x in s.split(' ') if x != '']
        return len(res[-1])
