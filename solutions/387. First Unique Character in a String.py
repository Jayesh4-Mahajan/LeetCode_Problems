class Solution:
    def firstUniqChar(self, s: str) -> int:
        # h = {}
        # res = -1
        # for i in range(len(s)):
        #     if s[i] not in h:
        #         h[s[i]] = i
        #     else:
        #         h[s[i]] = -1
        # for key in h.keys():
        #     if h[key] != -1:
        #         return h[key]
        # return -1
        
        from collections import Counter
        a = Counter(s)
        for i in range(len(s)):
            if a[s[i]] == 1:
                return i
        return -1
