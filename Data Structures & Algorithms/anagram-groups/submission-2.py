class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)
    
        # iterate through the array
        
        for s in strs:
            # calculate the key for each of the arrays   
            key = [0] * 26
            for c in s:
                bit = ord(c)-ord('a')
                key[bit]+=1
            # append to correct array
            d[tuple(key)].append(s)
        return list(d.values())