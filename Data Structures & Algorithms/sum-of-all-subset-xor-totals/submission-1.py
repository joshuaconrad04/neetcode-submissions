class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        if not nums:
            return 0

        res = 0

        
        def dfs(i, curr_sum):
            if i == len(nums):
                return curr_sum
            
            return dfs(i+1, curr_sum)+dfs(i+1, curr_sum^nums[i])
            
        return dfs(0,0)
            

            

            



        