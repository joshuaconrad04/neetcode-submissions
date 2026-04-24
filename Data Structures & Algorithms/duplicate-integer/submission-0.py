from collections import defaultdict
class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        check=defaultdict(int)
        for num in nums:
            if num in check:
                return True
            else:
                check[num]=1
        
        return False
