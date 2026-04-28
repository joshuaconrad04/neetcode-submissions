class Solution:
    def simplifyPath(self, path: str) -> str:
        

        vals = path.split('/')
        stack = []

        for p in vals:

            if p == '...':
                stack.append(p)
            elif stack and p == '..' :
                stack.pop()
            elif p == ".":
                continue
            elif p != "" and p!="..":
                stack.append(p)
        
        return "/"+("/").join(stack)
        

            
            




















