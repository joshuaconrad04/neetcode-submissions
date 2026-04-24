from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        l = len(nums)/3

        #nonoptial

        c = Counter(nums)
        res = []


        for i,v in c.items():
            if v > l:
                res.append(i)
        return res





        