from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # Skip duplicate elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            t = -nums[i]
            sol = self.twoSum(nums, i + 1, t)
            for pair in sol:
                res.append([nums[i]] + pair)
        return res

    def twoSum(self, nums: List[int], start: int, t: int) -> List[List[int]]:
        s, e = start, len(nums) - 1
        res = []
        while s < e:
            c = nums[s] + nums[e]
            if c == t:
                res.append([nums[s], nums[e]])
                # Skip duplicate elements
                while s < e and nums[s] == nums[s + 1]:
                    s += 1
                while s < e and nums[e] == nums[e - 1]:
                    e -= 1
                s += 1
                e -= 1
            elif c < t:
                s += 1
            else:
                e -= 1
        return res
