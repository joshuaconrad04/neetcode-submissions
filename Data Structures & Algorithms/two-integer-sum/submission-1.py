class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        #go through array and calculate what we're looking for basically, 

        #ie


        #we can see that target - arr[0] == 4, so we want a 4, if 4 is there, in the dict, so already seend
        #return the 2 indicies, else add the value that we found and it's indicie


        d = {}

        #iterate through array

        for i, num in enumerate(nums):

            #calcualte complement and check if its in dict

            complement = target-num

            if complement in d:
                return [d[complement], i]
            d[num]=i

        