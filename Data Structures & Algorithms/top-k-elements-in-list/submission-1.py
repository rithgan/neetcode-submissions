class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using bucket sort
        # create a freq map
        count = defaultdict(int)
        for n in nums:
            count[n]+=1
        freq = [[] for _ in range(len(nums)+1)]
        for n,cnt in count.items():
            freq[cnt].append(n)
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k: return res
        return res