import heapq
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:


        heapq.heapify(weight)
        min_heap = weight


        max_val = 5000
        apples = 0

        while min_heap:
            curr_val = heapq.heappop(min_heap)
            if max_val-curr_val >= 0:
                max_val = max_val - curr_val
                apples+=1
            else:
                return apples


        return apples
        