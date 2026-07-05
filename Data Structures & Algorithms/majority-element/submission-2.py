class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        mx = 0
        output = 0
        for n in nums:
            d[n]+=1
            if d[n]>=len(nums)//2:
                if d[n]>=mx:
                    mx = d[n]
                    output = n
        return output