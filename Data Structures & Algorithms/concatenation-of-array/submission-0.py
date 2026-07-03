class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans_len = 2 * len(nums)
        ans = [0] * ans_len
        for i,an in enumerate(nums):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]
        return ans