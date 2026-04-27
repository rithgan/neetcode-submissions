class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    maxSlidingWindow(nums, k) {
        let deque = new Array()
        let res = new Array()
        let l=0
        for (let r=0;r<nums.length;r++){
            while (deque.length && nums[deque[deque.length-1]] < nums[r]){
                deque.pop()
            }
            deque.push(r)
            if (l>deque[0]){
                deque.shift()
            }
            if (r+1 >=k ){
                res.push(nums[deque[0]])
                l++
            }
        }
        return res
    }
}
