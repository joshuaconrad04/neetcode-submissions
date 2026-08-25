class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]

        res = []
        for i, c in enumerate(strs[0]):
            for s in strs:
                if i==len(s) or c != s[i]:
                    return "".join(res)
            res.append(c)

        return "".join(res)


        
        