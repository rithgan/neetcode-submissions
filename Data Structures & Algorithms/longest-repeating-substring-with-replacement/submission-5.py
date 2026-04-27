class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        maxF = 0
        i=0
        for j in range(len(s)):
            count[s[j]] = 1+count.get(s[j],0)
            maxF = max(maxF,count[s[j]])
            while (j-i+1 - maxF) >k:
                count[s[i]]-=1
                i+=1
            res  = max(res,j-i+1)
        return res
