from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        #creating hashmap

        d = defaultdict(int)
        d[0] = 1
        res = 0
        curr_sum = 0

        for n in nums:
            curr_sum+=n
            target = (curr_sum-k)
            if target in d and d[target] >=1:
                res+=d[target]
            d[curr_sum]+=1


        return res


        
    
        


        