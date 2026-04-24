class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []


        def dfs(i, curr_arr):
            if len(curr_arr) == k:
                res.append(curr_arr.copy())
                return
            
            if i>n:
                return

            curr_arr.append(i)
            dfs(i+1, curr_arr)
            curr_arr.pop()
            dfs(i+1, curr_arr)
        
        dfs(1,[])
        return res
            

        