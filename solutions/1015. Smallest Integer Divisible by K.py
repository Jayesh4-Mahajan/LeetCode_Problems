class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1: return 1
        if k % 2 == 0: return -1
        modulo = set()
        num = 1
        while True:  
            mod = num % k
            if mod in modulo:
                return -1
            if mod != 0: 
                modulo.add(mod)
                num = num*10 + 1
            if mod == 0 and num >=k:
                return len(str(num))
        
            
