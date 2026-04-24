class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:



        prev  = -200
        diff =0

        for i in range(len(nums)):

            if nums[i] == prev:
                diff +=1
                prev = nums[i]
                nums[i] = 200
            else:
                prev = nums[i]
        nums.sort()
        return (len(nums)-diff)    


            

        