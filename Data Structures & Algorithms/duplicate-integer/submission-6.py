class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        d = defaultdict(int)
        for num in nums:
            if num in d:
                return True
            d[num]+=1
        return False