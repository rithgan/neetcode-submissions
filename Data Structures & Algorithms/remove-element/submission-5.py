class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        let's assume k is 0, and on every swap, we increase k+1
        we start two pointers, 1 from 0 and 1 from len(nums)-1
        if first is equal to val, we swap and increase +1, if last is val, we just increase by 1
        """
        i,j,k = 0,len(nums)-1,0
        while i<j:
            if nums[j]==val:
                # k+=1
                j-=1
            if nums[i]==val and nums[j]!=val:
                nums[i],nums[j] = nums[j], nums[i]
                # k+=1
                i+=1
                j-=1
                continue
            i+=1
            # k+=1
        for n in nums:
            if n!=val:
                k+=1
            if n==val:
                break
        return k