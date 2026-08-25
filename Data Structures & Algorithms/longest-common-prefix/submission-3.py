class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]

        shortest_string = sorted(strs)[0]

        res = []
        for i, c in enumerate(shortest_string):
            for s in strs:
                if c != s[i]:
                    return "".join(res)
            res.append(c)

        return "".join(res)


        
        