class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
​
        if "0000" in deadends or target in deadends:
            return -1
        visited = set() | set(deadends)
        visited.add("0000")
        q = deque([("0000", 0)])
        d = {str(i):[str((i+1)%10), str((i-1)%10)] for i in range(10)}
        while q:
            curr, steps = q.popleft()
            if curr == target:
                return steps
            for i in range(4):
                for digit in d[curr[i]]:
                    nextOpt = curr[:i]+digit+curr[i+1:]
                    if nextOpt not in visited:
                        visited.add(nextOpt)
                        q.append((nextOpt,steps+1))       
        return -1
                    
        
        
