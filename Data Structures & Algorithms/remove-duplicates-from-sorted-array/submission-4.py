class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        

        #part 1
        #create left pointer, start it at 1 bc the first value is always valid
        L=1

        #e.g = [1,1,2,3,4]
                  #L,R

        #start R and the same spot and keep iterating it, whenever you a find duplicate don't move L because we want to overwrite that spot, else you should move it +1

        for R in range(1, len(nums)):
            if nums[R] != nums[R-1]:
                nums[L]=nums[R]
                L+=1
        return L
        #at the end return L, because this will be end of array without duplicates