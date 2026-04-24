class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        

        s = set(nums)

        res = 1
        if 1 not in s:
            return 1

        while res+1 in s:
            res+=1
        return res+1