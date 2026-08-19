import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        neg_stones = [-i for i in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            s1 = -heapq.heappop(neg_stones)
            s2 = -heapq.heappop(neg_stones)
            if s1 == s2:
                continue
            elif s1 < s2:
                tmp = s2 - s1
                heapq.heappush(neg_stones, -tmp)
            else:
                tmp = s1 - s2
                heapq.heappush(neg_stones, -tmp)
        print(neg_stones)
        if neg_stones:
            return -neg_stones[0]
        else:
            return 0
        

        