class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        nums = new Set(nums)
        let longest = 0
        for (let num of nums){
            if (!nums.has(num-1)){
                let l = 1
                while (nums.has(num+l)){
                    l++
                }
                longest = Math.max(longest,l)

            }
        }
        return longest
    }
}
