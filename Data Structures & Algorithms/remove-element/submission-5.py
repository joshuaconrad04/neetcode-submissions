class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        for n in range(len(nums)):
            if nums[n]!=val:
                nums[i], nums[n] = nums[n], nums[i]
                i+=1

        return i
            




         
        