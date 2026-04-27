class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        if (s1.length>s2.length) return false;
        let count1 = new Array(26).fill(0)
        let count2 = new Array(26).fill(0)
        for (let i=0;i<s1.length;i++){
            count1[s1.charCodeAt(i)-97]++
            count2[s2.charCodeAt(i)-97]++
        }
        let matches = 0
        for (let i=0;i<26;i++) {
            if (count1[i]===count2[i]) {
                matches++
            }
        }
        let l=0
        for(let r=s1.length;r<s2.length;r++){
            if (matches === 26) return true
            // Add the new character (right pointer)
            let indexR = s2.charCodeAt(r) - 97;
            count2[indexR]++;
            if (count1[indexR] === count2[indexR]) {
                matches++;
            } else if (count1[indexR] + 1 === count2[indexR]) {
                matches--;
            }
            let indexL = s2.charCodeAt(l) - 97;
            count2[indexL]--;
            if (count1[indexL] === count2[indexL]) {
                matches++;
            } else if (count1[indexL] - 1 === count2[indexL]) {
                matches--;
            }
            l++
        }
        return matches === 26
    }
}
