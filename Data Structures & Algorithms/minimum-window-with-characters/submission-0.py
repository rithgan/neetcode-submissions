class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t): return ""
        if s == t: return s
        res = float("inf")
        st = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if Counter(t) <= Counter(s[i:j+1]):
                    if j-i+1 < res:
                        res = j-i+1
                        st = s[i:j+1] 
        return st if res != float('inf') else ""