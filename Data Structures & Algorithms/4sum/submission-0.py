class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        if len(nums) <4 :
            return res

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    for l in range(k+1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            res.add(tuple([nums[i], nums[j], nums[k],nums[l]]))


        return [list(i) for i in res]



        
        
                


            






        
        