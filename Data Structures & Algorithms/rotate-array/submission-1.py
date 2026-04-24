class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l=len(nums)

        tmp = nums.copy()

        for i in range(len(nums)):
            print(i, k, l)
            tmp[((i+k)%l)] = nums[i]
        
        
        for j in range(len(tmp)):
            nums[j] = tmp[j]
        
            
            

        