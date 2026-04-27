class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start,end=0,len(numbers)-1
        while start<end:
            sm = numbers[start]+numbers[end]
            if target==sm: return [start+1,end+1]
            if target>sm:
                start+=1
                continue
            else:
                end-=1
        return []