class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let res = 0
        let [l,r] = [0,heights.length-1]
        while (l<r){
            let area = Math.min(heights[l],heights[r])*(r-l)
            res = Math.max(res,area)
            if (heights[l]<heights[r]) l+=1
            else r-=1
        }
        return res
    }
}
