class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for st in strs:
            count = [0]*26
            for s in st:
                count[ord(s)-ord('a')]+=1
            mp[tuple(count)].append(st)
        return list(mp.values())