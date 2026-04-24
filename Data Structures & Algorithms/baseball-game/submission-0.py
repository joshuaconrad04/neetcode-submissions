class Solution:
    def calPoints(self, operations: List[str]) -> int:


        stack = []


        for l in operations:
            if l=="D":
                p = int(stack[-1])
                stack.append(p*2)
            elif l=="C":
                stack.pop()
            elif l=="+":
                p1 = stack[-1]
                p2 = stack[-2]
                stack.append(p1+p2)
            else:
                stack.append(int(l))
        return sum(stack)
        