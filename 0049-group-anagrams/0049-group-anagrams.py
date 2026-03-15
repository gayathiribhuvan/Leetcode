class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for i in strs:
            s = tuple(sorted(i))
            if s not in hashmap:
                hashmap[s] = [] 
            hashmap[s].append(i)
        return list(hashmap.values())