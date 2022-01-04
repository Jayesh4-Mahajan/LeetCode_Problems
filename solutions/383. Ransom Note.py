class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        for i in c1:
            if i not in c2:
                return False
            elif c2[i] < c1[i]:
                return False
            else:
                c2[i] -= c1[i]
        return True
